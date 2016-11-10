//1348 주차장


//max flow,이분매칭 + 이분탐색
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>
using namespace std;

typedef long long LL;
#define pii pair<int, int>
#define si(a) scanf("%d", &(a))
#define sc(a) scanf("%c", &(a))
#define ss(a) scanf("%s",a)
#define sLL(a) scanf("%lld", &(a))
#define pi(a) printf("%d\n", (a))
#define pc(a) printf("%c",a);
#define ENDL printf("\n");
#define pll(a) printf("%lld\n", (a))

#define INF 2e9
#define LLINF 1e16
#define all(a) (a).begin(), (a).end()
#define MAX_N 51

int n, m,ans;
int board[MAX_N][MAX_N];
int bar = 51;
vector<pii> G[10001];
vector<pii> car , park;

int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
vector<int>  back,check;

int dist[MAX_N][MAX_N];

void find(int x , int y,int start) {
	queue<pii> q;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			dist[i][j] = INF;
		}
	}
	dist[x][y] = 0;
	q.push(pii(x, y));
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int a = x + dx[i];
			int b = y + dy[i];
			if (a < 0 || a >= n || b < 0 || b >= m || board[a][b] == 'X') continue;

			if (dist[a][b] > dist[x][y] + 1) {
				q.push(pii(a, b));
				dist[a][b] = dist[x][y] + 1;
			}
		}
	}

	for (int i = 0; i < park.size(); i++) {
		int a = park[i].first;
		int b = park[i].second;
		G[start].push_back(pii(i,dist[a][b]));
	}
}


bool dfs(int cur,int x) {
	if (check[cur]) return false;

	check[cur] = true;
	for (int i = 0; i < G[cur].size(); i++) {
		int next = G[cur][i].first;
		int cost = G[cur][i].second;
		if (cost > x)continue;
		if (back[next] == -1 || dfs(back[next],x)) {
			back[next] = cur;
			return true;
		}
	}
	return false;
}

bool iscan(int x) {
	back = vector<int>(10001,-1);
	for (int i = 0; i < car.size(); i++) {
		check = vector<int>(10001, false);
		if (dfs(i,x) == false) 
			return false;
	}	
	return true;
}

int main() {
	si(n);
	si(m);

	for (int i = 0; i < n; i++) {
		char str[1234];
		ss(str);
		for (int j = 0; j < m; j++) {
			board[i][j] = str[j];
			if (str[j] == 'C') 	car.push_back(pii(i, j));
			if (str[j] == 'P') park.push_back(pii(i, j));
		}
	}

	for (int i = 0; i < car.size(); i++) {
		find(car[i].first, car[i].second, i);
	}
	if (car.size() == 0) {
		printf("0\n");
		return 0;
	}
	if (car.size() > park.size()) {
		printf("-1\n");
		return 0;
	}
	int lo = 0, hi = 10000;
	int ans = -1;
	while (lo <= hi) {
		int mid = (lo + hi) / 2;
		//printf("%d\n", mid);
		if (iscan(mid)) {
			ans = mid;
			hi = mid - 1;
		}
		else {
			lo = mid + 1;
		}
	}

	printf("%d\n", ans);
	return 0;
}
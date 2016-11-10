//2146 다리만들기

//그래프 순회 + 다잌스트라
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define ll				long long 
#define si(a)			scanf("%d",&(a))
#define sc(a)			scanf("%c",&(a))
#define ss(a)			scanf("%s",(a))

#define all(x)			(x).begin(),(x).end()
#define pii				pair<int, int>
#define inf				2e9

#define maxn			1001

int n,ans;
int map[123][123];
int check[123][123];
int landnum[123][123];
vector< vector< pii > > landset;
int dist[123][123];
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };

void findland(int x, int y, vector< pii > &land) {
	if (check[y][x])return;

	check[y][x] = true;
	land.push_back(pii(x, y));
	for (int i = 0; i < 4; i++) {
		int a = dx[i] + x;
		int b = dy[i] + y;

		if (a < 0 || a >= n || b < 0 || b >= n || map[b][a] == 0) continue;
		findland(a, b, land);		
	}
}

int findshort(vector< pii > &start, int startnum) {
	int ret = inf;
	queue< pii > q;
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++) 
			dist[i][j] = inf;
			
	for (int i = 0; i < start.size(); i++) {
		int x = start[i].first;
		int y = start[i].second;
		dist[y][x] = 0;
		q.push(pii(x, y));
	}
	
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second; 
		q.pop();

		for (int i = 0; i < 4; i++) {
			int a = dx[i] + x;
			int b = dy[i] + y;

			if (a < 0 || a >= n || b < 0 || b >= n) continue;
			if (dist[b][a] > dist[y][x] + 1) {
				dist[b][a] = dist[y][x] + 1;
				q.push(pii(a, b));
			}
		}
	}

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (map[i][j] == 1 && landnum[i][j] != startnum)
				ret = min(ret, dist[i][j]);
	
	return ret-1;
}

int main() {	
	ans = inf;
	si(n);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			si(map[i][j]);
	
	//find lands
	memset(check, 0, sizeof(check));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (check[i][j] == 1 || map[i][j] == 0) continue;
			vector< pii > temp;
			findland(j, i, temp);
			landset.push_back(temp);
		}
	}
	
	//landnum 
	for(int i = 0; i < landset.size(); i++) {
		for (int j = 0; j < landset[i].size(); j++) {
			int x = landset[i][j].first;
			int y = landset[i][j].second;
			landnum[y][x] = i + 1;
		}
	}
	
	//find ans
	int ans = inf;
	for (int i = 0; i < landset.size(); i++) {
		int val = findshort(landset[i], i+1);
		ans = min(ans, val);
	}
	
	printf("%d\n", ans);
	return 0;
}








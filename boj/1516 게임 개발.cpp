//1516 게임 개발
//코스트가 추가된 위상정렬 문제
//dp 스럽다
//각 건물이 만드는데 걸리는 최소 시간은 그전 건물들의 시간중에서 최대값이다

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>

#define ll long long
#define pii pair<int, int>
#define si(a) scanf("%d", &(a))
#define sc(a) scanf("%c", &(a))
#define ss(a) scanf("%s",a)
#define sll(a) scanf("%lld", &(a))
#define pi(a) printf("%d\n", (a))
#define pc(a) printf("%c",a);
#define ENDL printf("\n");
#define pll(a) printf("%lld\n", (a))

#define INF 2e9
#define all(a) (a).begin(),(a).end()
#define MAX_N 501

using namespace std;
int n;
vector<int> G[MAX_N];

int cost[MAX_N];
int totaltime[MAX_N];
int level[MAX_N];

int main() {
	int ans = INF;
	si(n);
	for (int i = 1, val; i <= n; i++) {
		si(val);
		cost[i] = val;
		while (1) {
			si(val);
			G[val].push_back(i);
			if (val == -1) break;
			level[i]++;
		}
	}

	queue<int>q;
	for (int i = 1; i <= n; i++) {
		if (level[i] == 0)q.push(i);
		totaltime[i] = cost[i];
	}

	while (!q.empty()) {
		int cur = q.front(); q.pop();

		for (int i = 0; i < G[cur].size(); i++) {
			int next = G[cur][i];
			level[next] --;
			totaltime[next] = max(totaltime[next], totaltime[cur] + cost[next]);
			if (level[next] == 0) {
				q.push(next);
			}
		}
	}

	for (int i = 1; i <= n; i++) {
		printf("%d\n", totaltime[i]);
	}
	return 0;
}

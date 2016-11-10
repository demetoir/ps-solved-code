//11408 열혈강호5

//mcmf 기본 구현
//단방향일때만 가능함

#include <stdio.h>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <string.h>
#include <set>
#include <map>
#include <unordered_map>
#include <functional>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9
#define MAXN			1001

int n, m;
vector<int> G[MAXN];
int cost[MAXN][MAXN];
int flow[MAXN][MAXN];
const int s = 0, t = 1000, bar = 500;
int ans = 0;
int maxflow = 0;
int main() {
	si(n); si(m);
	for (int i = 1,val; i <= n; i++) {
		si(val);
		for (int j = 0,a,b; j < val; j++) {
			si(a); si(b);
			a += bar;
			flow[i][a] = INF;
			G[i].push_back(a);
			cost[i][a] = b;
			//역방향간선
			G[a].push_back(i);
			cost[a][i] = -b;
		}
	}
	for (int i = 1; i <= n; i++) {
		G[s].push_back(i);
		G[i].push_back(s);
		cost[s][i] = 0;
		flow[s][i] = 1;
	}
	for (int i = 1; i <= m; i++) {
		G[i+bar].push_back(t);
		G[t].push_back(i+ bar);
		cost[i+bar][t] = 0;
		flow[i + bar][t] = 1;
	}

	while (1) {
		//find shortpath and cost
		vector<int>parent(MAXN, -1);
		vector<int>dist(MAXN, INF);
		queue<int> q;
		q.push(s);
		dist[s] = 0;
		while (!q.empty()) {
			int cur = q.front(); q.pop();
			
			for (int i = 0; i < G[cur].size(); i++) {
				int next = G[cur][i];
				//printf("@@@ %d %d :nextdist = %d, curdist = %d, c = %d , flow = %d\n", cur, next, dist[next],dist[cur], cost[cur][next], flow[cur][next]);
				if (flow[cur][next] > 0 && dist[next] > dist[cur] + cost[cur][next] ) {
					dist[next] = dist[cur] + cost[cur][next];
					parent[next] = cur;
					q.push(next);
					//printf("@@@ %d %d : %d\n", cur, next, dist[next]);
				}
			}
		}

		if (parent[t] == -1) break;

		// fill path and get max cost
		int curcost = 0;
		int minflow = INF;
		int cur = t;
		while (parent[cur] != -1) {
			int p = parent[cur];
			//printf("%d %d\n", cur, p);
			minflow = min(minflow, flow[p][cur]);
			cur = p;
		}
		//printf("%d\n", dist[t]);
		cur = t;
		while (parent[cur] != -1) {
			int p = parent[cur];
			curcost += cost[p][cur] * minflow;
			flow[p][cur] -= minflow;
			flow[cur][p] += minflow;
			cur = p;
		}
		maxflow += minflow;
		ans += curcost;
		//printf("$$$ %d %d <= +  %d %d\n\n", maxflow, ans, minflow, curcost);
	}

	printf("%d\n%d\n",maxflow, ans);
	return 0;
}


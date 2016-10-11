////1884 고속도로
//
////다잌스트라 응용
//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <functional>
//#include <utility>
//using namespace std;
//
//typedef long long LL;
//#define pii pair<int, int>
//#define si(a) scanf("%d", &(a))
//#define sc(a) scanf("%c", &(a))
//#define ss(a) scanf("%s",a)
//#define sLL(a) scanf("%lld", &(a))
//#define pi(a) printf("%d\n", (a))
//#define pc(a) printf("%c",a);
//#define ENDL printf("\n");
//#define pll(a) printf("%lld\n", (a))
//
//#define INF 2e9
//#define LLINF 1e16
//#define all(a) (a).begin(), (a).end()
//#define MAX_N 101
//
//int ans;
//int k, n, r;
//int dist[101][10001];
//struct edge {
//	int next, cost, money;
//	edge(int n, int c, int m):next(n), cost(c),money(m){}
//};
//vector<edge> G[MAX_N];
//
//int main() {
//	si(k);
//	si(n);
//	si(r);
//	for (int i = 0,s,d,l,t; i < r; i++) {
//		si(s); si(d); si(l); si(t);
//		G[s].push_back(edge(d, l, t));
//	}
//	for (int i = 0; i < 101; i++) {
//		for (int j = 0; j < 10001; j++) {
//			dist[i][j] = INF;
//		}
//	}
//	
//	queue<pii> q;
//	q.push(pii(1, 0));
//	dist[1][0] = 0;
//
//	while (!q.empty()) {
//		int cur = q.front().first;
//		int time = q.front().second;
//		q.pop();
//
//		for (int i = 0; i < G[cur].size(); i++) {
//			int next = G[cur][i].next;
//			int pluscost = G[cur][i].cost;
//			int plustime = G[cur][i].money;
//			if (time + plustime > k) continue;
//			
//			if (dist[next][time + plustime] > dist[cur][time] + pluscost) {
//				q.push(pii(next, time + plustime));
//				dist[next][time + plustime] = dist[cur][time] + pluscost;
//			}
//		}
//	}
//
//	int ans = INF;
//	for (int i = 0; i < 10001; i++) {
//		ans = min(dist[n][i], ans);
//	}
//
//	if (ans == INF)printf("-1\n");
//	else printf("%d\n", ans);
//
//
//
//	return 0;
//}

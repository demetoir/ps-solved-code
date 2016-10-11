////1760 N-Rook 
//
////maxflow 
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
//
//
//int n, m;
//int board[MAX_N][MAX_N];
//int R[MAX_N][MAX_N];
//int D[MAX_N][MAX_N];
//
//int s, t;
//struct Maxflow {
//	int size;
//	struct Edge {
//		int next;
//		int flow;
//		int rev_index;
//		Edge(int n, int f, int r) {
//			next = n;
//			flow = f;
//			rev_index = r;
//		}
//	};
//	vector< vector<Edge> > G;
//
//	Maxflow(int n) {
//		size = n;
//		G.assign(size, vector<Edge>());
//	}
//
//	void make_edge(int cur, int next, int flow, int rev_flow) {
//		Edge A(next, flow, G[next].size());
//		Edge B(cur, rev_flow, G[cur].size());
//		G[cur].push_back(A);
//		G[next].push_back(B);
//	}
//
//	int bfs(int s, int t) {
//		vector <pii> parent(size, pii(-1, -1));
//		vector <bool> check(size, false);
//		queue<int>q;
//		q.push(s);
//		check[s] = true;
//		while (!q.empty()) {
//			int cur = q.front(); q.pop();
//
//			for (int i = 0; i < G[cur].size(); i++) {
//				Edge &e = G[cur][i];
//
//				if (e.flow > 0 && check[e.next] == false) {
//					check[e.next] = true;
//					q.push(e.next);
//					parent[e.next].first = cur;
//					parent[e.next].second = i;
//				}
//			}
//		}
//
//		if (parent[t].first == -1) return 0;
//
//		int flow = INF;
//		for (int p = t; parent[p].first != -1; p = parent[p].first) {
//			Edge &e = G[parent[p].first][parent[p].second];
//			flow = min(flow, e.flow);
//		}
//
//		for (int p = t; parent[p].first != -1; p = parent[p].first) {
//			Edge &e = G[parent[p].first][parent[p].second];
//			e.flow -= flow;
//			G[e.next][e.rev_index].flow += flow;
//		}
//		return flow;
//	}
//
//	int getmaxflow(int s, int t) {
//		int maxflow = 0;
//		int flow = 0;
//		while (flow = bfs(s, t))
//			maxflow += flow;
//		return maxflow;
//	}
//};
//
//int main() {
//	si(n); si(m);
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			si(board[i][j]) ;
//		}
//	}
//	
//	s = 20001;
//	t = 20002;
//	//¿¬°á	
//	Maxflow mf(20003);
//
//
//	//¿·
//	int count = 1;
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			if (board[i][j] != 0 || R[i][j])continue;
//
//			for (int k = j; k < 1000; k++) {
//				if (k >= m) break;
//				if (board[i][k] == 2) break;
//				R[i][k] = count;
//			}
//			mf.make_edge(s, count, 1, 0);
//			count++;
//		}
//	}
//
//	count++;
//	//¾Æ·¡
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			if (board[i][j] != 0 || D[i][j] !=0)continue;
//
//			for (int k = i; k < 1000; k++) {
//				if (k >= n) break;
//				if (board[k][j] == 2) break;
//				D[k][j] = count;
//			}
//			mf.make_edge(count, t, 1, 0);
//			count++;
//		}
//	}
//	
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			if (board[i][j] != 0 )continue;
//			int a = R[i][j], b = D[i][j];
//			mf.make_edge(a, b, 1, 0);
//		}
//	}
//
//	int ans = mf.getmaxflow(s,t);
//	printf("%d\n", ans);
//	return 0;
//}

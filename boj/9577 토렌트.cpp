//9577 토렌트

//maxflow
//소스 -시간 -사람- 조각- 씽크
//    1    INF   INF   1
//
//
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>
#include <unordered_set>


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
#define MAX_N 3001

int bar1 = 200;
int bar2 = 400;
int s = 601;
int t = 602;
int n, m;
int ans;

//인접 리스트 버전
struct Maxflow {
	int size;
	struct Edge {
		int next;
		int flow;
		int rev_index;
		Edge(int n, int f, int r) {
			next = n;
			flow = f;
			rev_index = r;
		}
	};
	vector< vector<Edge> > G;

	Maxflow(int n) {
		size = n;
		G.assign(size, vector<Edge>());
	}

	void make_edge(int cur, int next, int flow, int rev_flow) {
		Edge A(next, flow, G[next].size());
		Edge B(cur, rev_flow, G[cur].size());
		G[cur].push_back(A);
		G[next].push_back(B);
	}

	int bfs(int s, int t) {
		vector <pii> parent(size, pii(-1, -1));
		vector <bool> check(size, false);
		queue<int>q;
		q.push(s);
		check[s] = true;
		while (!q.empty()) {
			int cur = q.front(); q.pop();
			for (int i = 0; i < G[cur].size(); i++) {
				Edge &e = G[cur][i];

				if (e.flow > 0 && check[e.next] == false) {
					check[e.next] = true;
					q.push(e.next);
					parent[e.next].first = cur;
					parent[e.next].second = i;
				}
			}
		}

		if (parent[t].first == -1) return 0;

		int flow = INF;
		for (int p = t; parent[p].first != -1; p = parent[p].first) {
			Edge &e = G[parent[p].first][parent[p].second];
			flow = min(flow, e.flow);
		}
		for (int p = t; parent[p].first != -1; p = parent[p].first) {
			Edge &e = G[parent[p].first][parent[p].second];
			e.flow -= flow;
			G[e.next][e.rev_index].flow += flow;
		}
		return flow;
	}

	int getmaxflow(int s, int t) {
		int maxflow = 0;
		int flow = 0;
		while (flow = bfs(s, t))
			maxflow += flow;
		return maxflow;
	}
};

int main() {
	int test; 
	si(test);
	for (; test > 0; test--) {
		si(n);
		si(m);
		Maxflow mf(603);
		for (int i = 0; i <= 100; i++)
			mf.make_edge(s, i, 1, 0);

		for (int i = 0; i < m; i++) {
			int  start, end,num;
			si(start); si(end);
			// 시간 - 사람
			for (int j = start; j < end; j++) {
				mf.make_edge(j, i + bar1, INF, 0);
			}

			si(num);
			//사람 - 조각
			for (int j = 0,val; j < num; j++) {
				si(val);
				mf.make_edge(i + bar1, val-1 + bar2, INF, 0);
			}	
		}
		//조각 씽크
		for (int i = 0; i < n; i++) {
			mf.make_edge(i + bar2, t, 1, 0);
		}

		ans = -1;
		int flow = mf.getmaxflow(s,t);
		//pi(flow);
		if (flow < n) {
			ans = -1;
		}
		else {
			for (int i = mf.G[s].size()-1 ; i >= 0; i--) {
				if (mf.G[s][i].flow == 0) {
					ans = i+1;
					break;
				}
			}
		}

		printf("%d\n", ans);
	}
	return  0;
}
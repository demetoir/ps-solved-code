//1658 돼지 잡기

//maxflow 
//s -(구매수)- 손님 --(열쇠 가지고있는 놈,INF)------------->> 우리 -(돼지수)-> t
//					<<--(마지막으로 우리를 열은 손님, inf)--
//양방향이기 때문에 인접 리스트로 한다


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
#define MAXN			1501

const int s = 0, t = MAXN - 1, bar = 200;

struct EDGE {
	int next, flow, revidx;
	EDGE() {};
	EDGE(int next, int flow, int revidx) :next(next), flow(flow), revidx(revidx) {};
};
int n, m;
vector<EDGE> G[MAXN];
int check[MAXN];
int last[MAXN];

void make_edge(int cur, int next, int flow, int revflow) {
	EDGE a(next, flow, G[next].size()), b(cur, revflow, G[cur].size());
	G[cur].push_back(a);
	G[next].push_back(b);
}

int getmaxflow() {
	int ret = 0;
	while (1) {
		//cur,idx
		vector<pii> parent(MAXN, pii(-1, -1));
		vector<int> check(MAXN, 0);
		queue<int> q;
		q.push(s);
		check[s] = 1;
		while (!q.empty()) {
			int cur = q.front(); q.pop();

			for (int i = 0; i < G[cur].size(); i++) {
				EDGE &e = G[cur][i];
				int next = e.next;
				int flow = e.flow;
				if (check[next] == 0 && flow) {
					parent[next] = pii(cur, i);
					check[next] = 1;
					q.push(next);
				}
			}
		}

		if (parent[t].first == -1) break;

		int flow = INF;
		int cur = t;
		while (parent[cur].first != -1) {
			EDGE &e = G[parent[cur].first][parent[cur].second];
			//printf("$$$ %d %d\n", parent[cur].first, e.next);
			flow = min(flow, e.flow);
			cur = parent[cur].first;
		}
		//printf("%d \n", flow);
		cur = t;
		while (parent[cur].first != -1) {
			EDGE &e = G[parent[cur].first][parent[cur].second];
			e.flow -= flow;
			G[e.next][e.revidx].flow += flow;
			cur = parent[cur].first;
		}

		ret += flow;
	}
	return ret;
}

int main() {
	si(m); si(n);

	memset(last, -1, sizeof(last));
	// 우리 - t
	for (int i = 1, val; i <= m; i++) {
		si(val);
		make_edge(i + bar, t, val, 0);
	}

	for (int i = 1, buy, A; i <= n; i++) {
		si(A);
		//손놈 - 우리
		for (int j = 0, next; j < A; j++) {
			si(next);
			make_edge(i, next + bar, INF, 0);
			if (last[next] != -1) make_edge(next + bar, last[next], INF, 0);
			last[next] = i;
		}
		// s  - 손놈
		si(buy);
		make_edge(s, i, buy, 0);
	}

	int ans = getmaxflow();
	printf("%d\n", ans);

	return 0;
}


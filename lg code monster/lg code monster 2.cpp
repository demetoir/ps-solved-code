//code moster 2
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

#pragma warning(disable:4996)
#define LL				long long 
#define pii				pair<int, int>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define sLL(a)			scanf("%lld", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N			10001
#define pb(a)			push_back((a))

LL ans;
int n, m, q;
int uftree[10001];
int ranktree[10001];
int find(int x) {
	if (x == uftree[x]) return x;
	return uftree[x] = find(uftree[x]);
}
void unite(int a, int b) {
	int A = find(a), B = find(b);
	if (A == B)return;
	if (ranktree[A] <= ranktree[B]) {
		uftree[B] = A;
		if (ranktree[A] == ranktree[B]) ranktree[B]++;
	}
	else {
		uftree[A] = B;
	}
}
struct S {
	int a, b, c;
	S(int a, int b, int c) :a(a), b(b), c(c) {}
};
bool cmp(S a, S b) {
	return a.c > b.c;
}

vector<S> edgelist;
vector <pii> spantree[10001];
int G[1234][1234];
void make_spaning_tree() {
	int cnt = 0;
	sort(all(edgelist), cmp);
	for (int i = 0; i < edgelist.size(); i++) {
		if (cnt == n - 1)
			break;
		int a = edgelist[i].a;
		int b = edgelist[i].b;
		int c = edgelist[i].c;

		if (find(a) == find(b)) continue;

		unite(a, b);
		spantree[a].pb(pii(b, c));
		spantree[b].pb(pii(a, c));
		cnt++;
	}
	return;
}

LL check[10001];
LL mbf;
bool dfs(int x, int end) {
	if (check[x])return false;
	check[x] = true;
	if (x == end) return true;

	for (int i = 0; i < spantree[x].size(); i++) {
		int next = spantree[x][i].first;
		LL cost = spantree[x][i].second;

		if (dfs(next, end)) {
			if (mbf > cost)	mbf = cost;
			return true;
		}
	}
	return false;
}
LL get_mbp(int s, int t) {
	memset(check, 0, sizeof(check));
	mbf = INF;
	if (s == t) return 0;
	dfs(s, t);
	return mbf;
}

int main() {
	int test;
	for (si(test); test > 0; test--) {
		edgelist.clear();
		ans = 0;
		memset(G, 0, sizeof(G));
		for (int i = 0; i <= 10000; i++) {
			spantree[i].clear();
			uftree[i] = i;
			ranktree[i] = 0;
		}

		si(n); si(m);
		for (int i = 0, a, b, c; i < m; i++) {
			si(a); si(b); si(c);
			if (G[a][b] < c) G[a][b] = c;
			if (G[b][a] < c) G[b][a] = c;
		}

		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < n + 1; j++) {
				if (i == j) continue;
				if (G[i][j] == 0)continue;
				edgelist.pb(S(i, j, G[i][j]));
			}
		}

		make_spaning_tree();

		si(q);
		for (int a, b; q > 0; q--) {
			si(a); si(b);
			LL val = get_mbp(a, b);
			ans += val;
			//printf("## %d %d %d", a, b, val);
		}

		printf("%lld\n", ans);
	}
	return 0;
}

//2000985283
//1000
//947327
//2000996518
//1000
//1000
//2000534656
//2000997214
//2000996855
//10000993287
//1000
//2000527251
//2000968639
//2000997217
//1000
//6000993151
//998205
//2000996369
//557998
//2000994963

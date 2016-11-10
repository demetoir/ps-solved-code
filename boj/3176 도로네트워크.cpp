//3176 도로 네트워크

lca + rmq
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define LL				long long 
#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define all(x)			(x).begin(),(x).end()
#define pii				pair<int, int>
#define INF				2e9

#define MAXN			100001
#define BITSIZE			21

int n,m;
vector<pii> G[MAXN];
vector<int>parent, check, depth;
int LCA[MAXN][BITSIZE];
int minmemo[MAXN][BITSIZE];
int maxmemo[MAXN][BITSIZE];
void dfs(int cur, int level) {
	check[cur] = 1;
	depth[cur] = level;
	for (int i = 0; i < G[cur].size(); i++) {
		int next = G[cur][i].first;
		int cost = G[cur][i].second;
		if (check[next]) continue;

		parent[next] = cur;
		LCA[next][0] = cur;
		minmemo[next][0] = cost;
		maxmemo[next][0] = cost;
		for (int b = 1; b < BITSIZE; b++) {
			LCA[next][b] = LCA[LCA[next][b - 1]][b - 1];
			minmemo[next][b] = min(minmemo[next][b - 1], minmemo[LCA[next][b - 1]][b - 1]);
			maxmemo[next][b] = max(maxmemo[next][b - 1], maxmemo[LCA[next][b - 1]][b - 1]);
		}
		dfs(next, level + 1);
	}
}

int minq(int a, int b) {
	if (depth[a] < depth[b])swap(a, b);
	int minval = INF;

	for (int i = BITSIZE - 1; i >= 0; i--) {
		if ((1 << i) <= depth[a] - depth[b]) {
			minval = min(minval, minmemo[a][i]);
			a = LCA[a][i];
		}
	}
	if (a == b)return minval;

	for (int i = BITSIZE - 1; i >= 0; i--) {
		if (LCA[a][i] != LCA[b][i]) {
			minval = min(minval, minmemo[a][i]);
			minval = min(minval, minmemo[b][i]);
			a = LCA[a][i];
			b = LCA[b][i];
		}
	}
	minval = min(minmemo[a][0], minval);
	minval = min(minmemo[b][0], minval);
	return minval;
}

int maxq(int a, int b) {
	if (depth[a] < depth[b])swap(a, b);
	int maxval = -1;
	for (int i = BITSIZE - 1; i >= 0; i--) {
		if ((1 << i) <= depth[a] - depth[b]) {
			maxval = max(maxval, maxmemo[a][i]);
			a = LCA[a][i];
		}
	}
	if (a == b)return maxval;

	for (int i = BITSIZE - 1; i >= 0; i--) {
		if (LCA[a][i] != LCA[b][i]) {
			maxval = max(maxval, maxmemo[a][i]);
			maxval = max(maxval, maxmemo[b][i]);
			a = LCA[a][i];
			b = LCA[b][i];
		}
	}
	maxval = max(maxmemo[a][0], maxval);
	maxval = max(maxmemo[b][0], maxval);
	return maxval;
}


int main() {
	si(n);
	check = vector<int>(n + 1);
	parent = vector<int>(n + 1);
	depth = vector<int>(n + 1);
	memset(LCA, 0, sizeof(LCA));
	for (int i = 0; i < MAXN; i++) {
		for (int j = 0; j < BITSIZE; j++) {
			minmemo[i][j] = INF;
			maxmemo[i][j] = -1;
		}
	}

	for (int i = 0,a,b,c; i < n - 1; i++) {
		si(a); si(b); si(c);
		G[a].push_back(pii(b, c));
		G[b].push_back(pii(a, c));
	}
	dfs(1, 1);



	si(m);
	for (int i = 0, a, b; i < m; i++) {
		si(a); si(b);
		int minval=0, maxval=0;
		minval = minq(a, b);
		maxval = maxq(a, b);
		printf("%d %d\n", minval, maxval);
	}


	return 0;
}







////11438 lca2
//
////lca O(logn)
//#include <iostream>
//#include <stdio.h>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <string.h>
//#include <string>
//using namespace std;
//
//
//#define LL				long long 
//#define si(a)			scanf("%d",&(a))
//#define ss(a)			scanf("%s",(a))
//#define all(x)			(x).begin(),(x).end()
//#define pii				pair<int, int>
//
//
//#define MAXN			100001
//#define bitsize			21
//vector<int> G[MAXN], check, parent, depth;
//int memo[MAXN][bitsize];
//int n, m;
//
//void dfs(int cur, int level) {
//	check[cur] = true;
//	depth[cur] = level;
//	for (int i = 0; i < G[cur].size(); i++) {
//		int next = G[cur][i];
//		if (check[next])continue;
//		parent[next] = cur;
//
//		memo[next][0] = cur;
//		for (int b = 1; b < bitsize; b++) {
//			memo[next][b] = memo[memo[next][b - 1]][b - 1];
//		}
//		dfs(next, level+1);
//	}
//}
//int lca(int a, int b) {
//	if (depth[a] < depth[b])swap(a, b);
//
//	for (int i = bitsize - 1; i >= 0; i--) {
//		if ((1 << i) <= depth[a] - depth[b]) {
//			a = memo[a][i];
//		}
//	}
//	if (a == b)return a;
//
//	for (int i = bitsize - 1; i >= 0; i--) {
//		if (memo[a][i] != memo[b][i]) {
//			a = memo[a][i];
//			b = memo[b][i];
//		}
//	}
//	return memo[a][0];
//}
//
//int main() {
//	si(n);
//	check = vector<int>(n + 1);
//	parent = vector<int>(n + 1); 
//	depth = vector<int>(n + 1); 
//	memset(memo, 0, sizeof(memo));
//	for (int i = 0,a,b; i < n - 1; i++) {
//		si(a); si(b);
//		G[a].push_back(b);
//		G[b].push_back(a);
//	}
//	dfs(1, 1);
//	si(m);
//	for (int i = 0, a, b; i < m; i++) {
//		si(a); si(b);
//		int ans = lca(a, b);
//		printf("%d\n", ans);
//	}
//	return 0;
//}
//
//
//
//
//
//

////1761 정점들의 거리
//
////lca
////총거리 = 루트-a  + 루트-b - 루트-lca(a,b)*2
//
//#include <iostream>
//#include <stdio.h>
//#include <vector>
//#include <queue>
//#include <algorithm>
//using namespace std;
//
//
//#define LL				long long 
//#define si(a)			scanf("%d",&(a))
//#define ss(a)			scanf("%s",(a))
//#define all(x)			(x).begin(),(x).end()
//#define MAXN			52345
//#define pii				pair<int, int>
//int n, m;
//
//vector<pii>  G[MAXN];
//vector<int> check,depth,parent,pathsum;
//void init() {
//	check = vector<int>(n + 1);
//	parent = vector<int>(n + 1);
//	depth = vector<int>(n + 1);
//	pathsum = vector<int>(n + 1);
//}
//void dfs(int cur, int level, int sum) {	
//	check[cur] = 1;
//	depth[cur] = level;
//	pathsum[cur] = sum;
//	for (int i = 0; i < G[cur].size(); i++) {
//		int next = G[cur][i].first;
//		int cost = G[cur][i].second;
//		if (check[next]) continue;
//		parent[next] = cur;		
//		dfs(next, level + 1,sum+ cost);
//	}
//}
//
//int lca(int a, int b) {
//	if (depth[a] < depth[b]) swap(a, b);
//
//	while (!(depth[a] == depth[b])) a = parent[a];
//
//	while (!(a == b)) {
//		a = parent[a];
//		b = parent[b];
//	}
//	return a;
//}
//
//
//int main() {
//	si(n);
//	for (int i = 0, a, b,c; i < n-1; i++) {
//		si(a); si(b); si(c);
//		G[a].push_back(pii(b,c));
//		G[b].push_back(pii(a,c));
//	}
//	init();
//	dfs(1, 1, 0);
//
//	si(m);
//	for (int i = 0,a,b; i < m; i++) {
//		si(a); si(b);
//		int val = lca(a, b);
//		int ans = pathsum[a] + pathsum[b] - pathsum[val] * 2;
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

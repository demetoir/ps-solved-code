
//11437 lca
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


#define LL				long long 
#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define all(x)			(x).begin(),(x).end()
#define MAXN			52345
int n, m;
vector<int>  G[MAXN],check,depth,parent;
void init() {
	check = vector<int>(n + 1);
	parent = vector<int>(n + 1);
	depth = vector<int>(n + 1);
}
void dfs(int cur, int level) {	
	check[cur] = 1;
	depth[cur] = level;
	for (int i = 0; i < G[cur].size(); i++) {
		int next = G[cur][i];
		if (check[next]) continue;
		parent[next] = cur;		
		dfs(next, level + 1);
	}
}
int lca(int a, int b) {
	if (depth[a] < depth[b]) swap(a, b);

	while (!(depth[a] == depth[b])) a = parent[a];

	while (!(a == b)) {
		a = parent[a];
		b = parent[b];
	}
	return a;
}
int main() {
	si(n);
	for (int i = 0, a, b; i < n-1; i++) {
		si(a); si(b);
		G[a].push_back(b);
		G[b].push_back(a);
	}
	init();
	dfs(1, 1);

	si(m);
	for (int i = 0,a,b; i < m; i++) {
		si(a); si(b);
		int val = lca(a, b);
		printf("%d\n", val);
	}


	return 0;
}
//2150 Strongly Connected Component

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
#define sc(a)			scanf("%c",&(a))
#define ss(a)			scanf("%s",(a))

#define all(x)			(x).begin(),(x).end()
#define pii				pair<int, int>
#define INF				2e9

#define MAXN			10001
vector< vector<int> > scc;

int n, m;
vector<int> G[MAXN], revG[MAXN];
int check[MAXN];
vector<int> vcheck;

void numbering_dfs(int cur) {
	if (check[cur]) return;
	check[cur] = true;

	for (int i = 0; i < G[cur].size(); i++) {
		int next = G[cur][i];
		numbering_dfs(next);
	}
	vcheck.push_back(cur);
}

void unite_dfs(int cur, vector<int> &cc) {
	if (check[cur]) return;
	check[cur] = true;

	for (int i = 0; i < revG[cur].size(); i++) {
		int next = revG[cur][i];
		unite_dfs(next, cc);
	}
	cc.push_back(cur);
}

bool cmp(const vector<int> &a, const vector<int> &b) {
	return a[0] < b[0];
}

int main() {
	si(n); si(m);
	for (int i = 0, a, b; i < m; i++) {
		si(a); si(b);
		G[a].push_back(b);
		revG[b].push_back(a);
	}

	memset(check, 0, sizeof(check));
	for (int i = 1; i <= n; i++)
		numbering_dfs(i);

	memset(check, 0, sizeof(check));
	reverse(all(vcheck));
	for (int i = 0; i < n; i++) {
		int start = vcheck[i];
		vector<int> cc;
		unite_dfs(start, cc);
		if (cc.size() > 0) {
			sort(all(cc));
			scc.push_back(cc);
		}
	}

	sort(all(scc), cmp);
	printf("%d\n", scc.size());
	for (int i = 0; i < scc.size(); i++) {
		for (int j = 0; j < scc[i].size(); j++) {
			printf("%d ", scc[i][j]);
		}
		printf("-1\n");
	}

	return 0;
}








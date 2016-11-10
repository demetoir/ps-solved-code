//2224 명제 증명

//
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <functional>
#include <stdio.h>
#include <deque>
using namespace std;

#define LL				long long 
#define pii				pair<int, int>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N			10001


int n, m, k;
vector<int> A,v;
vector< int >  G[128];
char check[128];
bool dfs(int x, int end) {
	if (check[x])
		return false;
	check[x] = 1;
	if (x == end)
		return true;
	for (int i = 0; i < G[x].size(); i++) {
		int next = G[x][i];
		if (dfs(next, end)) return true;
	}
	return false;
}
int main() {
	si(n);
	scanf("\n");
	for (int i = 0; i < n; i++) {
		char a, b;
		scanf("%c => %c\n", &a, &b);
		G[a].push_back(b);
	}
	vector<pii> v;
	for (int i = 0; i <128; i++) {
		for (int j = 0; j < 128; j++) {
			if (i == j) continue;
			memset(check, 0, sizeof(check));
			if (dfs(i, j))
				v.push_back(pii(i, j));
		}
	}
	sort(all(v));

	printf("%d\n", v.size());
	for (int i = 0; i < v.size(); i++) {
		printf("%c => %c\n", v[i].first, v[i].second);
	}



	return 0;

}

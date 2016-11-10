//1743 음식물 피하기

#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

#pragma warning(disable:4996)
#define LL				long long 
#define pii				pair<int, int>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N			10001

int n,m,k,ans;
int map[123][123];
int check[123][123];
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };

int dfs(int x, int y) {
	if (check[x][y]) return 0;
	check[x][y] = 1;

	int ret = 1;
	for (int i = 0; i < 4; i++) {
		int a = x + dx[i];
		int b = y + dy[i];
		if (a < 0 || a >= n || b < 0 || b >= m || map[a][b] == 0) continue;

		ret += dfs(a, b);
	}
	return ret;
}
int main() {
	si(n);	si(m);	si(k);
	for (int i = 0,a,b; i < k; i++) {
		si(a);	si(b);
		map[a-1][b-1] = 1;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (check[i][j] == 0 && map[i][j] == 1)
				ans = max(ans, dfs(i, j));
		}
	}
	
	printf("%d\n", ans);
	return 0;
}

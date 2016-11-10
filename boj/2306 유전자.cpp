//2306 유전자 

//dp 와리가리
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>
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
#define MAX_N 501

int ans;

char str[MAX_N];
int dp[MAX_N][MAX_N];
int find(int x, int y) {
	if (x > y)return 0;
	if (x == y) return 0;
	if (dp[x][y] != -1)
		return dp[x][y];
		
	int ret = 0;
	if ((str[x] == 'a' && str[y] == 't') ||
		(str[x] == 'g' && str[y] == 'c') ){
		ret = max(ret, find(x + 1, y - 1) + 2);
	}
	for (int i = x; i < y; i++)
		ret = max(ret, find(x, i) + find(i + 1, y));

	dp[x][y] = ret;
	//printf("%d %d : %d\n", x, y, ret);
	return ret;
}
int main() {
	ss(str);
	int size = strlen(str);
	for (int i = 0; i < MAX_N; i++) {
		for (int j = 0; j < MAX_N; j++) {
			dp[i][j] = -1;
		}
	}

	ans = find(0, size - 1);
	printf("%d\n", ans);
	return 0;
}

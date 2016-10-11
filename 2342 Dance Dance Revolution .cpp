////2342 Dance Dance Revolution 
//
////dp 
//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <functional>
//#include <utility>
//using namespace std;
//
//typedef long long LL;
//#define pii pair<int, int>
//#define si(a) scanf("%d", &(a))
//#define sc(a) scanf("%c", &(a))
//#define ss(a) scanf("%s",a)
//#define sLL(a) scanf("%lld", &(a))
//#define pi(a) printf("%d\n", (a))
//#define pc(a) printf("%c",a);
//#define ENDL printf("\n");
//#define pll(a) printf("%lld\n", (a))
//
//#define INF 2e9
//#define LLINF 1e16
//#define all(a) (a).begin(), (a).end()
//#define MAX_N 100001
//
//
//LL n, k, ans;
//
//int cost[5][5] = {
//	{1,2,2,2,2},
//	{3,1,3,4,3},
//	{3,3,1,3,4},
//	{3,4,3,1,3},
//	{3,3,4,3,1}
//};
//int dp1[5][5];
//int dp2[5][5];
//
//int main() {
//	for (int i = 0; i < 5; i++)
//		for (int j = 0; j < 5; j++)
//			dp1[i][j] = INF;
//
//	int cur = 0, pre = 0;
//
//	si(cur);
//	pre = cur;
//	dp1[cur][0] = dp1[0][cur] = cost[0][cur];
//
//	while (1) {
//		si(cur);
//		if (cur == 0) break;
//		pre = cur;
//		for (int i = 0; i < 5; i++)
//			for (int j = 0; j < 5; j++)
//				dp2[i][j] = INF;
//
//		for (int i = 0; i < 5; i++) {
//			for (int j = 0; j < 5; j++) {
//				if (i == cur || i == j) continue;
//				dp2[cur][i] = min(dp2[cur][i], dp1[j][i] + cost[j][cur]);
//				dp2[i][cur] = min(dp2[i][cur], dp1[i][j] + cost[j][cur]);
//				//printf("%d %d  <- %d %d == %d  %d\n", cur, i, i, j , dp2[cur][i], dp2[i][cur]);
//			}
//		}
//
//		for (int i = 0; i < 5; i++)
//			for (int j = 0; j < 5; j++)
//				dp1[i][j] = dp2[i][j];
//	}
//	int ans = INF;
//	for (int i = 0; i < 5; i++) {
//		ans = min(ans, dp1[pre][i]);
//		ans = min(ans, dp1[i][pre]);
//	}
//	printf("%d\n", ans);
//	return 0;
//}

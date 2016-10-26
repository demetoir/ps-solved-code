////1082 방번호
//
////조합탐색...
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <queue>
//#include <functional>
//#include <math.h>
//using namespace std;
//
//#pragma warning(disable:4996)
//#define LL				long long 
//#define pii				pair<int, int>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define sLL(a)			scanf("%lld", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)			(a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAXN			100001
//#define pb(a)			push_back((a))
//
//int n;
//int num[123];
//int k = 0;
//int ans[123];
//int minval = INF;
//bool isfirst = true;
//void find(int cur, int cost) {
//	if (cur == 0) return;
//
//	for (int i = n - 1; i >= 0; i--) {
//		if ((cur - 1) * minval <= cost - num[i]) {
//			if (isfirst && i == 0)continue;
//			isfirst = false;
//			ans[cur] = i;
//			find(cur - 1, cost - num[i]);
//			return;
//		}
//	}
//
//	ans[cur] = -1;
//	find(cur - 1, cost);	
//}
//int main() {
//	while (scanf("%d",&n) >0) {
//		minval = INF;
//		isfirst = true;
//		for (int i = 0; i < 123; i++)ans[i] = -1;
//
//		for (int i = 0; i < n; i++) {
//			si(num[i]);
//			minval = min(minval, num[i]);
//		}
//
//		si(k);
//		find(50, k);
//		if (ans[1] == -1) {
//			printf("0\n");
//			continue;
//		}
//
//		for (int i = 123 -1; i >= 0; i--) {
//			if (ans[i] == -1) continue;
//			printf("%d", ans[i]);
//		}
//		printf("\n");
//	}
//	return 0;
//}

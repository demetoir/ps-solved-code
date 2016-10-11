//
////1300 k번째수
//
////이분탐색
//
//
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
//LL n, k,ans;
//bool find(LL x) {
//	LL ret = 0;
//	for (int i = 1; i <= n; i++) {
//		ret += min(x / i , n);
//	}
//	if (ret >= k)return true;
//	return false;
//}
//int main() {
//	sLL(n);	sLL(k);	
//	bool isfind = false;
//
//	LL lo = 0, hi = LLINF;
//	while (lo <= hi) {
//		LL mid = (lo + hi) / 2;
//		//printf("%lld\n",mid);
//		if (find(mid)) {
//			ans = mid;
//			hi = mid - 1;
//		}
//		else {
//			lo = mid + 1;
//		}
//	}
//
//
//	printf("%lld\n", ans);
//	return 0;
//}

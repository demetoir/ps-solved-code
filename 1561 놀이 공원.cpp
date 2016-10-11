//
////1561 ³îÀÌ °ø¿ø
//
////ÀÌºÐ Å½»ö
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
//#define MAX_N 10001
//int ans;
//int n, m;
//int A[MAX_N];
//bool find(LL x) {
//	LL sum = 0;
//	for (int i = 0; i < m; i++){
//		sum += x / A[i];
//	}
//	if (sum >= n)return true;
//	return false;
//}
//int main() {
//	si(n); si(m);
//	for (int i = 0; i < m; i++) si(A[i]);
//
//	if (m >= n) {
//		printf("%d\n", n);
//		return  0;
//	}
//	n -= m;
//
//	LL lo = 0, hi = LLINF;
//	LL time = LLINF;
//	while (lo <= hi) {
//		LL mid = (lo + hi) / 2;
//		//pll(mid);
//		if (find(mid) ) {
//			hi = mid - 1;
//			time = mid;
//		}
//		else {
//			lo = mid + 1;
//		}
//	}
//
//	//printf("\n");
//	//pll(time);
//	int sum = 0;
//	for (int i = 0; i < m; i++) sum += time / A[i];
//	for (int i = m-1; i>=0; i--) {
//		if (time % A[i] == 0) {
//			if (sum == n)
//				ans = i+1;
//			sum--;
//		}
//	}
//
//
//
//	printf("%d\n",ans);
//
//	return 0;
//}
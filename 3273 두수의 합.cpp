////3273 두수의 합
//
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <queue>
//#include <functional>
//using namespace std;
//
//#pragma warning(disable:4996)
//#define LL				long long 
//#define pii				pair<int, int>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)			(a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAX_N			10001
//#define pb(a)			push_back((a))
//int n, x;
//int A[123456];
//int main() {
//	si(n);
//	for (int i = 0,val; i < n; i++) si(A[i]);	
//	si(x);
//
//	sort(A,A+n);
//	LL ans = 0;
//	for (int i = 0; i < n; i++) {
//		int val = upper_bound(A + i + 1, A + n, x - A[i]) - lower_bound(A + i + 1, A + n, x - A[i]);
//		//printf("%d %d\n", i, val);
//		ans += val;
//	}
//	printf("%lld\n", ans);
//
//
//	return 0;
//}

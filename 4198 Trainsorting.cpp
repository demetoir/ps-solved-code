////4198 Trainsorting
//#include <iostream>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <string.h>
//#include <functional>
//#include <stdio.h>
//#include <deque>
//using namespace std;
//#define LL              long long 
//#define pii             pair<long long, long long>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define sll(a)          scanf("%lld", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)  (a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAX_N 123456
//
//
//int n;
//int A[12345];
//int main() {
//	si(n);
//	for (int i = 0; i < n; i++) {
//		si(A[i]);
//	}
//	vector<int> lis(4000),lds(4000);
//	for (int start = n - 1; start >= 0; start--) {
//		lis[start] = 1;
//		for (int i = start + 1; i < n; i++) {
//			if (A[start] < A[i]) lis[start] = max(lis[start], lis[i] + 1);
//		}
//		lds[start] = 1;
//		for (int i = start + 1; i < n; i++) {
//			if (A[start] > A[i]) lds[start] = max(lds[start], lds[i] + 1);
//		}
//	}
//	int ans = 0;
//	for (int i = 0; i < n; i++) {
//		ans = max(lds[i] + lis[i] - 1, ans);
//	}
//
//	printf("%d \n", ans);
//	return 0;
//}

////1485 정사각형
//
//// 기하
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
//#define MAX_N 501
//
//pii A[4];
//int main() {
//
//	int test;
//	for (si(test); test > 0; test--) {
//		int ans = 0;
//		for (int i = 0, a, b; i < 4; i++) {
//			si(a); si(b);
//			A[i] = pii(a, b);
//		}
//		LL ret = 0;
//
//		sort(A, A + 4);
//		vector<int> B;
//		for (int i = 0; i < 4; i++) {
//			for (int j = i+1; j < 4; j++) {
//			
//				LL val = (A[i].first - A[j].first)*(A[i].first - A[j].first);
//				val+= (A[i].second - A[j].second)*(A[i].second - A[j].second);
//				B.push_back(val);
//			}
//		}
//		sort(all(B));
//		B.erase(unique(all(B)), B.end());
//		if (B.size() == 2) ans = 1;
//		printf("%d\n", ans);
//	}
//	return 0;
//}

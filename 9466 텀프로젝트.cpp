////9466 텀프로젝트
////사이클 판별 
////구현이 지랄맞다
//
////https://www.acmicpc.net/problem/9466
//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <functional>
//#include <utility>
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
//#define LLINF 1e17
//#define all(a) (a).begin(), (a).end()
//#define MAX_N 100001
//
//using namespace std;
//#define MOD 360000
//
//LL n;
//int A[MAX_N];
//int check[MAX_N];
//int iscycle[MAX_N];
//
//int main() {	
//	int test = 0; si(test);
//	for (; test > 0; test--) {
//		int ans = 0;
//		si(n);
//		memset(check, 0, sizeof(check));
//		memset(A, 0, sizeof(A));
//
//		for (int i = 1; i <= n; i++) {
//			si(A[i]);
//			iscycle[i] = -1;
//		}
//		for (int i = 1; i <= n; i++) {
//			if (check[i]) continue;
//			int x = i;
//
//			bool flag = false;
//			while (1) {
//				//새로운데서 끝남
//				if (check[x] && iscycle[x] == -1)
//					break;
//				
//				//했던데서 끝남
//				if (check[x] && iscycle[x] != -1) {
//					flag = true;
//					break;
//				}
//				check[x] = 1;
//				x = A[x];
//			}
//			
//			if (flag) {
//				x = i;
//				while (1) {
//					if (iscycle[x] != -1) break;
//					iscycle[x] = 0;
//					x = A[x];
//				}
//			}
//			else {				
//				while (1) {
//					if (iscycle[x] == 1) break;
//					iscycle[x] = 1;
//					x = A[x];
//				}
//
//				x = i;
//				while (1) {
//					if (iscycle[x] != -1) break;
//					iscycle[x] = 0;
//					x = A[x];
//				}
//			}
//		}
//
//		for (int i = 1; i <= n; i++) {
//			if (iscycle[i] == 0)ans++;
//		}
//		printf("%d\n", ans);
//
//	}
//	return 0;
//}

//// 4243 보안 업체
////
////
////dp 와리가리, 아이디어, 군수열?? 상상
////일단 와리가리 dp이다
////존나 개같다 멍멍 왈왈 
////
////점화식을 구하는 거는 쉬운데 누적합이기 떄문에 매번 더할 조각 값을 구하는거가 힘들었다
////단순히 매 단계에서 최소 지연시간이나 최소 누적 시간을
////마지막 단계만 우리가 구하려는 최적값이 나오고 중간 단계의 값이 실제 중간 단계의 최적값이 아닌 dp 이다
////매 단계에서 구하는거가  그단계까지의 누적합의 이 아니라 전체 조각에대해 끝까지 더해주는 값을 이 조각이다
////예제 케이스를 보면
////1
////1 2
////1 2 2 1 4
////1 2 2 1 4 7
////이런식으로 매단계까지 걸리는 시간이 이렇게 걸리면
////누적합은
////1 + 1 2 + 1 2 2 1 4 + 1 2 2 1 4 7
////이렇게 되는데
////각각 
////1 이 4번
////2 이 3번
////2 1 4 이 2번
////7 이 1번
////이렇게 되기때문에 
////매번 더하는 조각 = 매번 추가 되는 양 * 반복되는 횟수
////따라서 
////dleft[i][j] = min( dright[i+1][j] + 조각 , dleft[i+1][j] + 조각)
////
////dright[i][j] = min( dright[i][j-1] + 조각 , dleft[i][j-1] + 조각 )
//
//#include <iostream>
//#include <cstdio>
//#include <string>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <functional>
//#include <utility>
//#include <limits.h>
//
//typedef long long LL;
//using namespace std;
//
//#define pii pair<int, int>
//#define PLL pair<LL,LL>
//#define si(a) scanf("%d", &(a))
//#define sc(a) scanf("%c", &(a))
//#define ss(a) scanf("%s",a)
//#define sll(a) scanf("%lld", &(a))
//#define pi(a) printf("%d\n", (a))
//#define pc(a) printf("%c",a);
//#define ENDL printf("\n");
//#define pll(a) printf("%lld\n", (a))
//#define INF 2e9
//#define LLINF 1e17 
//#define all(a) (a).begin(),(a).end()
//
//#define MAX_N 101
//
//LL t[MAX_N];
//LL n, a;
//LL ans;
//
////누적합
//LL dpl[MAX_N][MAX_N];
//LL dpr[MAX_N][MAX_N];
//
//int main() {
//	int test = 0;
//	for (si(test); test > 0; test--) {
//		sll(n);
//		sll(a);
//		for (int i = 1; i < n; i++) {
//			sll(t[i]);
//		}
//		for (int i = 0; i <= 100; i++) {
//			for (int j = 0; j <= 100; j++) {
//				dpl[i][j] = LLINF;
//				dpr[i][j] = LLINF;
//			}
//		}
//
//		dpl[a][a] =0;
//		dpr[a][a] = 0;
//
//		for (int len = 1; len < n ; len++) {
//			for (int i = 1; i <= n; i++) {
//				int j = i + len;
//				if (j > n) continue;
//
//				LL sum = 0,l,r;
//				for (int k = i; k < j; k++) sum += t[k];
//
//				//dpl
//				l = dpl[i + 1][j] + t[i]*(n-len );
//				r = dpr[i + 1][j] + sum *(n - len );
//				dpl[i][j]= min(l,r);
//				//dpr
//				l = dpl[i][j-1] + sum*(n-len);
//				r = dpr[i][j-1]+ t[j-1]*(n - len);
//				dpr[i][j]= min(l,r);
//				//printf("##L %lld %lld %lld \n", i, j, dpl[i][j]);
//				//printf("##R %lld %lld %lld \n", i, j, dpr[i][j]);
//			}
//		}
//		
//		ans = min(dpl[1][n],dpr[1][n]);	
//		pll(ans);
//	}
//	return 0;
//}

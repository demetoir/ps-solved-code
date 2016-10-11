////4095 최대 정사각형
//#include <stdio.h>
//#include <algorithm>
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
//
//
//int n, m;
//int map[1234][1234];
//
//int main() {
//	while (1) {
//		si(n); si(m);
//		if (n == 0 && m == 0) break;
//
//		int ans = 0;
//		for (int i = 0; i < n; i++) {
//			for (int j = 0; j < m; j++) {
//				si(map[i][j]);
//				ans = max(ans, map[i][j]);
//			}
//		}
//
//		for (int i = 1; i < n; i++) {
//			for (int j = 1; j < m; j++) {
//				if (map[i][j] == 0) continue;
//				map[i][j] = min(map[i - 1][j] + 1, map[i][j - 1] + 1);
//				map[i][j] = min(map[i - 1][j - 1] + 1, map[i][j]);
//				ans = max(map[i][j], ans);
//			}
//		}
//		printf("%d\n", ans);
//	}
//	return 0;
//}

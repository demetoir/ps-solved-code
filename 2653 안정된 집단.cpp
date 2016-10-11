////2653 안정된 집단
//
////아이디어..
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
//
//#define INF             2e9
//#define LLINF			1e17
//#define MAX_N 123456
//
//int n;
//int G[101][101];
//int cnt[101];
//int main() {
//	si(n);
//
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < n; j++) {
//			si(G[i][j]);
//		}
//	}
//
//	int c = 1;
//	for (int i = 0; i < n; i++) {
//		if (cnt[i] > 0) continue;
//		for (int j = i+1; j < n; j++) {
//			bool f = true;
//			for (int k = 0; k < n; k++) {
//				if (G[i][k] != G[j][k])f = false;
//			}
//			if (f) {
//				cnt[j] = c;
//				cnt[i] = c;
//			}
//		}
//		c++;
//	}
//
//	for (int i = 0; i < n; i++) {
//		if (cnt[i] == 0) {
//			printf("0\n");
//			return 0;
//		}
//	}
//
//
//	printf("%d\n", c-1);
//	for (int i = 1; i < c+1; i++) {
//		for (int j = 0; j < n; j++)
//			if (cnt[j] == i)
//				printf("%d ", j+1);
//		printf("\n");
//	}
//
//
//	return 0;
//}
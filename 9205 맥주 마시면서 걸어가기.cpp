////9205 맥주 마시면서 걸어가기
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
//int n, m, k;
//int ans;
//int u, l, r, d;
//int grid[123][123];
//
//int main() {
//	int test;
//	si(test);
//	int a, b, c, d;
//	for (; test > 0; test--) {
//
//		si(n);
//		si(a); si(b);
//		vector<pii> v;
//		for (int i = 0, a, b; i < n; i++) {
//			si(a); si(b);
//			v.push_back(pii(a, b));
//		}
//		si(c); si(d);
//
//		queue<pii>q;
//		q.push(pii(a, b));
//		vector<int> check(n + 1);
//		int ans = false;
//		while (!q.empty()) {
//			int x = q.front().first;
//			int y = q.front().second;
//			q.pop();
//
//			if (abs(c - x) + abs(d - y) <= 1000) {
//				ans = true;
//			}
//
//			for (int i = 0; i < n; i++) {
//				if (check[i]) continue;
//				if (abs(v[i].first - x) + abs(v[i].second - y) <= 1000) {
//					q.push(pii(v[i]));
//					check[i] = true;
//				}
//			}
//		}
//		if (ans) printf("happy\n");
//		else printf("sad\n");
//
//	}
//
//
//	return 0;
//
//}
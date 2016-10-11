////2343 기타 레슨
//
////이분탐색 그리디
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
//
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
//
//vector<int> v;
//
//int find(int x) {
//	int cur = 0, count = 0;
//	for (int i = 0; i < n; i++) {
//		if (v[i] > x)return false;
//		 
//		if (cur + v[i] <= x) 
//			cur += v[i];		
//		else {
//			cur = v[i];
//			count++;
//		}			
//	}
//
//	if (cur != 0)count++;
//	if (count > m)return false;
//	return true;
//
//}
//
//int main() {
//	si(n); si(m);
//	for (int i = 0,val; i < n; i++) {
//		si(val);
//		v.push_back(val);
//	}
//
//	LL lo = 0, hi = INF;
//	int ans = INF;
//	while (lo <= hi) {
//		int mid = (lo + hi) / 2;
//		//printf("%d\n", mid);
//		if (find(mid)) {
//			ans = mid;
//			hi = mid - 1;
//		}
//		else
//			lo = mid + 1;
//	}
//
//	printf("%d\n", ans);
//	return 0;
//
//}

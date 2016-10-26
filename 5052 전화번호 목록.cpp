////5052 전화번호 목록
//
//#include <iostream>
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <set>
//#include <string>
//#include <functional>
//#include <queue>
//using namespace std;
//
//typedef long long int LL;
//typedef pair<int, int> pii;
//typedef pair<LL, LL> pll;
//struct mp {
//	int a, b;
//	mp() {}
//	mp(int a, int b) :a(a), b(b) {};
//};
//
//#define si(a)			scanf("%d",&(a))
//#define ss(a)			scanf("%s",(a))
//#define all(x)			(x).begin(),(x).end()
//
//int ans = 0;
//int n;
//vector<string>v;
//char str[12345];
//int main() {
//	int test = 0;
//	si(test);
//	for (; test > 0; test--) {
//		v.clear();
//		si(n);
//
//		for (int i = 0; i < n; i++) {
//			ss(str);
//			string s(str);
//			v.push_back(s);
//		}
//
//		sort(all(v));
//
//		int ans = true;
//		for (int i = 0; i < n - 1; i++) {
//			int a = v[i].size();
//			int b = v[i + 1].size();
//			int size = min(a, b);
//			bool f = true;
//			for (int j = 0; j < size; j++) {
//				if (v[i +1][j] != v[i][j]) {
//					f = false;
//					break;
//				}
//			}
//			if (f) 	ans = false;
//		}
//
//		if (ans) printf("YES\n");
//		else printf("NO\n");
//	}
//
//}
//
//
//
//
//
//

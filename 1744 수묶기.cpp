////1744 수묶기
//
////그리디
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
//	mp(){}
//	mp(int a, int b) :a(a), b(b) {};
//};
//
//#define si(a)			scanf("%d",&(a))
//#define all(x)			(x).begin(),(x).end()
//
//int ans = 0;
//int n;
//int main() {
//	priority_queue <int> pq;
//	priority_queue <int, vector<int>, greater<int> > pq2;
//
//
//	si(n);
//	int zero = 0;
//	for (int i = 0,val; i < n; i++) {
//		si(val);
//		if(val>0)
//			pq.push(val);
//		if (val < 0)
//			pq2.push(val);
//		if (val == 0)zero++;
//	}
//
//
//	while (pq.size() >= 2) {
//		int a = pq.top(); pq.pop();
//		int b = pq.top(); pq.pop();
//		if (a*b <= a+b) {
//			pq.push(a);
//			pq.push(b);
//			break;
//		}
//		ans += a*b;
//	}
//	
//	while (pq2.size() >= 2) {
//		int a = pq2.top(); pq2.pop();
//		int b = pq2.top(); pq2.pop();
//		if (a*b <= a + b) {
//			pq2.push(a);
//			pq2.push(b);
//			break;
//		}
//		ans += a*b;
//	}
//
//	while (!pq.empty()) {
//		ans += pq.top();
//		pq.pop();
//	}
//
//	while (!pq2.empty()) {
//		if (zero > 0) {
//			zero--;
//		}
//		else {
//			ans += pq2.top();
//		}
//		pq2.pop();
//	}
//
//	printf("%d\n", ans);
//	return 0;
//}
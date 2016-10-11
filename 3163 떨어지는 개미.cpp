//// 3163 떨어지는 개미
//
//
////아이디어
////시간이 지나도 개미의 아이디순서는 그대로 
////따라서 먼저 떨어지는 순서대로 왼쪽에서 떨어지는지 오른쪽에서 떨어지는지 검사해서 답을고른다
////동시에 떨어질때는 따로 처리한다 
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
//#define MAX_N 100001
//
//LL ans;
//
//vector<PLL> ant;
//int n,k,l;
//bool cmp(PLL a, PLL b) {
//	if (a.first != b.first) return a.first < b.first;
//	return a.second > b.second;
//}
//int main() {
//	int test = 0;
//	for (si(test); test > 0; test--) {
//		si(n); si(l); si(k);
//		ant.clear();
//		deque< int>deq;
//		for (int i = 0,a,p; i < n; i++) {
//			si(p); si(a);
//			if (a > 0)
//				ant.push_back(PLL(l - p, a));
//			else
//				ant.push_back(PLL(p, a));
//			deq.push_back(a);
//		}
//		sort(all(ant));
//		
//		for (int i = 0; i < k; i++) {
//			if (ant[i].first == ant[i + 1].first) {
//				if (deq.front() > deq.back()) {
//					swap(ant[i], ant[i + 1]);
//				}
//			}
//
//			if (ant[i].second > 0) {
//				ans = deq.back();
//				deq.pop_back();
//			}
//			else {
//				ans = deq.front();
//				deq.pop_front();
//			}
//			//printf("$$"); pi(ans);
//			
//		}
//		printf("%lld\n", ans);
//	}
//	return 0;
//}

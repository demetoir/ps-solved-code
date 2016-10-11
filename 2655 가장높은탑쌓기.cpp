////2655 가장높은탑쌓기 
//
////dp로도 할수있을거같은데
////일단은 다잌으로 풀었다
////dp로할려면 순서를 알야아하는데 소트를 어떻게 잘하면 될것같은제 확실하지않다
////다잌으로 푸는데 -가중치 곱하고 모든 정점에서 시작했다.
//
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <queue>
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
//int n;
//struct S {
//	int l, h, w,num;
//	S(int l,int h, int w, int num):l(l),h(h),w(w),num(num){}
//};
//vector<S>v;
//
//int main() {
//	si(n);
//	for (int i = 0,a,b,c; i < n; i++) {
//		si(a); si(b); si(c);
//		v.push_back(S(a, -b, c, i));
//	}
//	queue <int> q;
//	vector<int> dist(123, 0);
//	vector<int> parent(123, -1);
//	for (int i = 0; i < n; i++) q.push(i);	
//	
//	while (!q.empty()) {
//		int cur = q.front(); q.pop();
//
//		for (int next = 0; next < n; next++) {
//			if (v[next].l < v[cur].l && v[next].w < v[cur].w) {
//				if (dist[next] > dist[cur] + v[next].h) {
//					dist[next] = dist[cur] + v[next].h;
//					parent[next] = cur;
//					q.push(next);
//				}
//			}
//		}
//	}
//
//	int minval = 0;
//	int idx = -1;
//	for (int i = 0; i < n; i++) {
//		if (minval > dist[i]) {
//			minval = dist[i];
//			idx = i;
//		}
//	}
//	int ans = 0;
//	int cur = idx;
//	while (cur != -1) {
//		cur = parent[cur];
//		ans += 1;
//	}
//
//	printf("%d\n", ans);
//	while (idx != -1) {
//		printf("%d\n", idx+1);
//		idx = parent[idx];
//	}
//
//	return 0;
//}

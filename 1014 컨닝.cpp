//
////1014 컨닝
////최대 독립 집합 maxflow ,이분 매칭
//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <functional>
//#include <utility>
//using namespace std;
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
//#define LLINF 1e16
//#define all(a) (a).begin(), (a).end()
//#define MAX_N 81
//int ans;
//
//vector< vector<int> > G;
//int n, m;
//int board[MAX_N][MAX_N];
//int dx[6] = { -1, 0, 1, -1, 0, 1 };
//int dy[6] = { -1, -1, -1, 1, 1, 1 };
//
//vector<int> check, back;
//bool dfs(int cur) {
//	if (check[cur])return false;
//	check[cur] = true;
//
//	for (int i = 0; i < G[cur].size(); i++) {
//		int next = G[cur][i];
//		if (back[next] == -1 || dfs(back[next])) {
//			back[next] = cur;
//			return true;
//		}
//	}
//	return false;
//}
//int match() {
//	int ret = 0;
//	back.assign(n*m + 1, -1);
//
//	for (int i = 0; i < n*m; i++) {
//		check.assign(n*m + 1, false);
//		if (dfs(i)) ret++;
//	}
//	return ret;
//}
//int main() {
//	int test = 0;
//	int count = 0;
//	for (si(test); test > 0; test--) {
//		count = 0;
//		si(n); si(m);
//		G.assign(10000, vector<int>());
//		for (int i = 0; i < n; i++) {
//			char str[1234];
//			ss(str);
//			for (int j = 0; j < m; j++) 
//				board[i][j] = str[j];
//			
//		}
//		for (int i = 0; i < n; i++) {
//			for (int j = 0; j < m; j++) {
//				if (board[i][j] == 'x') continue;
//				count++;
//				int cur = i + j*n;
//				for (int k = 0; k < 6; k++) {
//					int x = i + dx[k];
//					int y = j + dy[k];
//					int next = x + y*n;
//					if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] == 'x') continue;
//
//					G[cur].push_back(next);
//				}
//			}
//		}
//		int ans = match();
//
//
//		printf("%d\n",count - ans/2);
//	}
//	return 0;
//}
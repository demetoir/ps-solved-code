//
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
//#define pii				pair<int, int>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)			(a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAX_N			123456
//
//
//int n, m, k;
//int dx[4] = { 0,1,0,-1 };
//int dy[4] = { 1,0,-1,0 };
//char map[123][123];
//int check[123][123];
//
//void dfs(int x, int y, vector<pii> &G) {
//	if (check[y][x]) return;
//	check[y][x] = 1;
//
//	G.push_back(pii(x, y));
//	for (int i = 0; i < 4; i++) {
//		int a = x + dx[i], b = y + dy[i];
//		if (a < 0 || a >= m + 2 || b < 0 || b >= n + 2) continue;
//		if (map[b][a] == '*')continue;
//		dfs(a, b, G);
//	}
//	return;
//}
//
//bool cmp(vector<pii> &a, vector<pii> &b) {
//	return a.size() < b.size();
//}
//int main() {
//	si(n); si(m); si(k);
//	memset(map, '.', sizeof(map));
//	for (int i = 0; i < n; i++) {
//		char str[123];
//		ss(str);
//		for (int j = 0; j < m; j++) {
//			map[i + 1][j + 1] = str[j];
//		}
//	}
//
//	vector < vector<pii> > G;
//	vector<pii>o;
//	dfs(0, 0, o);
//	for (int i = 0; i < n + 2; i++) {
//		for (int j = 0; j < m + 2; j++) {
//			if (map[i][j] == '.' && check[i][j] == 0) {
//				vector <pii> g;
//				dfs(j, i, g);
//				G.push_back(g);
//			}
//		}
//	}
//
//	sort(all(G), cmp);
//	int ans = 0;
//	for (int idx = 0, count = G.size(); count > k; count--, idx++) {
//		ans += G[idx].size();
//		for (int i = 0; i < G[idx].size(); i++) {
//			int x = G[idx][i].first;
//			int y = G[idx][i].second;
//			map[y][x] = '*';
//		}
//	}
//
//	printf("%d\n", ans);
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < m; j++) {
//			printf("%c", map[i + 1][j + 1]);
//		}
//		printf("\n");
//	}
//	return 0;
//}

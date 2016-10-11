////code moster 2
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <queue>
//#include <math.h>
//#include <functional>
//using namespace std;
//
//#pragma warning(disable:4996)
//#define LL				long long 
//#define pii				pair<int, int>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define sLL(a)			scanf("%lld", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)			(a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAX_N			10001
//#define pb(a)			push_back((a))
//
//int n, startidx;
//vector<pii> P, Q;
//vector<int>hay, pattern;
//int ccw(int idx, vector<pii> &v) {
//	pii p1 = v[idx];
//	pii p2 = v[(idx + 1) % n];
//	pii p3 = v[(idx + 2) % n];
//	int ret = (p2.first - p1.first)*(p3.second - p1.second) - (p2.second - p1.second)*(p3.first - p1.first);
//
//	if (ret > 0) return 1;
//	if (ret < 0) return -1;
//	return 0;
//}
//
//vector<int> make_Pie(vector<int> &pattern) {
//	int size = pattern.size();
//	vector<int>pie(size);
//
//	int start = 1, matched = 0;
//	while (start + matched < size) {
//		if (pattern[start + matched] == pattern[matched]) {
//			matched += 1;
//			pie[start + matched - 1] = matched;
//		}
//		else {
//			if (matched == 0)start += 1;
//			else {
//				start += matched - pie[matched - 1];
//				matched = pie[matched - 1];
//			}
//		}
//	}
//	return pie;
//}
//
//int kmp(vector<int> &hay, vector<int> &pattern) {
//	int h = hay.size();
//	int n = pattern.size();
//	int ret = 0;
//
//	vector<int> pie = make_Pie(pattern);
//	int matched_count = 0;
//	int start = 0, matched = 0;
//	while (start <= h - n) {
//		if (matched < n && hay[start + matched] == pattern[matched]) {
//			matched += 1;
//			if (matched == n) ret++;
//		}
//		else {
//			if (matched == 0) start++;
//			else {
//				start += matched - pie[matched - 1];
//				matched = pie[matched - 1];
//			}
//		}
//	}
//	return ret;
//}
//
//int getd(pii a, pii b) {
//	if (a.first == b.first)
//		return abs(a.second - b.second);
//	else
//		return abs(a.first - b.first);
//}
//
//vector<pii> rotate(vector<pii> &v) {
//
//}
//
//bool issim(vector<pii>&v1, vector<pii> &v2) {
//	vector<pii> Aset;
//
//	for (int i = 0; i < n; i++) {
//
//		if (ccw(i, v1) == 1) {
//			Aset[i].first = (i - 1 + n) % n;
//		}
//		else {
//			int val = INF;
//			int idx = 0;
//			for (int j = 0; j < n; j++) {
//				if (j == (i - 1 + n) % n) continue;
//				if (v1[i].first == v1[(i + 1) % n].first  && v1[j].first != v1[(j + 1) % n].first) {
//					if (val > v1[j].second) {
//						val = v1[j].second;
//						idx = j;
//					}
//				}
//
//				if (v1[i].second == v1[(i + 1) % n].second  && v1[j].second != v1[(j + 1) % n].second) {
//					if (val > v1[j].first) {
//						val = v1[j].first;
//						idx = j;
//					}
//				}
//			}
//			Aset[i].first = idx;
//		}
//
//		if (ccw((i + 1) % n, v1) == 1) {
//			Aset[(i + 1) % n].first = (i + 1 + n) % n;
//		}
//		else {
//			int val = INF;
//			int idx = 0;
//			for (int j = 0; j < n; j++) {
//				if (j == (i + 1 + n) % n) continue;
//				if (v1[i].first == v1[(i + 1) % n].first  && v1[j].first != v1[(j + 1) % n].first) {
//					if (val > v1[j].second) {
//						val = v1[j].second;
//						idx = j;
//					}
//				}
//
//				if (v1[i].second == v1[(i + 1) % n].second  && v1[j].second != v1[(j + 1) % n].second) {
//					if (val > v1[j].first) {
//						val = v1[j].first;
//						idx = j;
//					}
//				}
//			}
//			Aset[i].first = idx;
//		}
//
//	}
//
//
//}
//
//
//
//int main() {
//	int test;
//	for (si(test); test > 0; test--) {
//		si(n);
//		P.clear(); Q.clear();
//		for (int i = 0, a, b; i < n; i++) {
//			si(a); si(b);
//			P.push_back(pii(a, b));
//		}
//		for (int i = 0, a, b; i < n; i++) {
//			si(a); si(b);
//			Q.push_back(pii(a, b));
//		}
//		int val = 0;
//
//		hay.clear(); pattern.clear();
//		for (int i = 0; i < n; i++) {
//			hay.push_back(getd(Q[i], Q[(i + 1) % n]) * ccw(i, Q));
//			pattern.push_back(getd(P[i], P[(i + 1) % n])*ccw(i, P));
//		}
//		for (int i = 0; i < n; i++) hay.push_back(hay[i]);
//
//		val = kmp(hay, pattern);
//		if (val) {
//			printf("1\n");
//			continue;
//		}
//
//		hay.clear(); pattern.clear();
//		for (int i = 0; i < n; i++) {
//			hay.push_back(ccw(i, Q));
//			pattern.push_back(ccw(i, P));
//		}
//		for (int i = 0; i < n; i++) hay.push_back(hay[i]);
//
//		val = kmp(hay, pattern);
//		if (val) {
//			printf("0\n");
//			continue;
//		}
//
//		printf("-1\n");
//	}
//	return 0;
//}
//
//
//

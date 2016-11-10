//2465 줄세우기

//세그먼트트리 + 이분탐색 + 좌표 압축
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <functional>
#include <stdio.h>
#include <deque>
using namespace std;
#define LL              long long 
#define pii             pair<long long, long long>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define sll(a)          scanf("%lld", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)  (a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N 123456


vector<int> v;
vector<int> tree;
int ans[123456];
int A[123456];
int find(int node, int s, int e, int val) {
	if (s == e) {
		return s;
	}
	int mid = (s + e) / 2;
	if (val <= tree[node * 2]) {
		return find(node * 2, s, mid, val);
	}
	else {
		return find(node * 2 + 1, mid + 1, e, val - tree[node * 2]);
	}
}

void update(int node, int s, int e, int idx, int diff) {
	if (idx < s || e < idx)return;
	tree[node] += diff;
	if (s == e)  return;
	int mid = (s + e) / 2;
	update(node * 2, s, mid, idx, diff);
	update(node * 2 + 1, mid + 1, e, idx, diff);
}

int main() {
	int n;
	si(n);
	int h = ceil(log2(n)) + 1;
	int treesize = 1 << (h + 1);
	tree = vector<int>(treesize + 1);

	for (int i = 0, val; i < n; i++) {
		si(val);
		v.push_back(val);
	}
	sort(all(v));
	for (int i = 0; i < n; i++)	update(1, 0, n - 1, i, 1);

	for (int i = 0, val; i < n; i++) si(A[i]);

	for (int i = n - 1; i >= 0; i--) {
		int idx = find(1, 0, n - 1, A[i] + 1);
		ans[i] = v[idx];
		update(1, 0, n - 1, idx, -1);
	}

	for (int i = 0; i < n; i++) printf("%d\n", ans[i]);	

	return 0;
}
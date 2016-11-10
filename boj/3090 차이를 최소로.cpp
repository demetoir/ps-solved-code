//3090 차이를 최소로

#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

#pragma warning(disable:4996)
#define LL				long long 
#define pii				pair<int, int>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N			10001

int n, t;
vector<int>v;

int find(LL x, vector<int> &A) {
	int cnt = 0;
	for (int i = 0; i < n-1; i++) {
		if (A[i] < A[i + 1] && A[i+1] - A[i] > x) {
			int diff = A[i + 1] - A[i] -x;
			A[i + 1] -= diff;
			cnt += diff;
		}
	}

	for (int i = n - 1; i > 0; i--) {
		if (A[i] < A[i - 1] && A[i-1] - A[i] > x) {
			int diff = A[i - 1] - A[i] - x;
			A[i-1] -= diff;
			cnt += diff;
		}
	}
	return cnt;
}
int main() {
	si(n); si(t);
	for (int i = 0,val; i < n; i++) {
		si(val);
		v.push_back(val);
	}

	LL lo = 0, hi = INF;
	LL ans = 0;
	vector<int> ansv;
	while (lo<=hi) {
		LL mid = (lo + hi) / 2;
		vector<int> A = v;
		LL cnt = find(mid,A);
	
		if (cnt <= t) {
			ans = mid;
			hi = mid - 1;
			ansv = A;
		}
		else
			lo = mid + 1;
	}

	for (int i = 0; i < n; i++)
		printf("%d ", ansv[i]);

	return 0;
}

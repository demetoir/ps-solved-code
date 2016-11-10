//9015 정사각형

//기하
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>
#include <unordered_set>


using namespace std;

typedef long long LL;
#define pii pair<int, int>
#define si(a) scanf("%d", &(a))
#define sc(a) scanf("%c", &(a))
#define ss(a) scanf("%s",a)
#define sLL(a) scanf("%lld", &(a))
#define pi(a) printf("%d\n", (a))
#define pc(a) printf("%c",a);
#define ENDL printf("\n");
#define pll(a) printf("%lld\n", (a))

#define INF 2e9
#define LLINF 1e16
#define all(a) (a).begin(), (a).end()
#define MAX_N 3001

int ans = 0;
int n;
pii A[MAX_N];
int mul = 30000;
unordered_set <int> set;

int main() {
	int test = 0;
	si(test);
	for (; test > 0; test--) {
		ans = 0;
		si(n);
		set.clear();
		for (int i = 0; i < n; i++) {
			si(A[i].first); si(A[i].second);
			set.insert(A[i].first * mul + A[i].second);
		}


		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				pii a = A[i], b = A[j];
				if (a == b) continue;

				int x = a.second - b.second;
				int y = a.first - b.first;
				if (set.find((a.first - x) * mul + a.second + y) != set.end() &&
					set.find((b.first - x) * mul + b.second + y) != set.end()) {
					int val = (a.first - b.first)* (a.first - b.first) +
						(a.second - b.second) * (a.second - b.second);
					if (ans < val) ans = val;
				}

				if (set.find((a.first + x) * mul + a.second - y) != set.end() &&
					set.find((b.first + x) * mul + b.second - y) != set.end()) {
					int val = (a.first - b.first)*  (a.first - b.first) +
						(a.second - b.second) * (a.second - b.second);
					if (ans < val) ans = val;
				}
			}
		}

		printf("%d\n", ans);
	}

	return 0;
}
//2842 집배원 한상덕

//bfs + bianary search
//모든 low val에하여  hival 을 탐색한다
//더빠른 해답이 존재한다

#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <string.h>
#include <set>
#include <map>
#include <functional>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9
#define MAXN			51

int n;
int ll[MAXN][MAXN];
char cll[MAXN][MAXN];
int check[MAXN][MAXN];
int sx, sy;
int K;
int ans = INF;
bool bfs(int lo, int hi) {
	queue<pii> q;
	q.push(pii(sx, sy));
	int k = K;
	memset(check, 0, sizeof(check));
	check[sy][sx] = 1;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int i = -1; i <= 1; i++) {
			for (int j = -1; j <= 1; j++) {
				int a = x + i;
				int b = y + j;
				if (a < 0 || a >= n || b < 0 || b >= n || check[b][a] == 1) continue;
				if (ll[b][a] < lo || ll[b][a] > hi) continue;

				check[b][a] = 1;
				if (cll[b][a] == 'K') k--;
				q.push(pii(a, b));
			}
		}
	}

	if (k) return false;
	return true;
}

vector<int> v;
int main() {
	si(n);

	int start = INF, end = 0;
	for (int i = 0; i < n; i++){
		ss(cll[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			si(ll[i][j]);
			v.push_back(ll[i][j]);
			if (cll[i][j] == 'P') {
				sx = j;
				sy = i;
				start = min(ll[i][j], start);
				end = max(ll[i][j], end);
			}				
			if (cll[i][j] == 'K') {
				K++;
				start = min(ll[i][j], start);
				end = max(ll[i][j], end);
			}
		}
	}

	sort(all(v));
	v.erase(unique(all(v)), v.end());
	int lowidx = lower_bound(all(v), start) - v.begin();
	for (; lowidx >= 0; lowidx--) {
		int lowval = v[lowidx];
		
		int lo = end;
		int hi = v[v.size()-1];
		int val = INF;
		while (lo <= hi) {
			int mid = (hi + lo) / 2;

			if (bfs(lowval, mid)) {
				hi = mid - 1;
				val = mid;
			}
			else {
				lo = mid + 1;
			}
		}
		ans = min(val - lowval, ans);
	}

	printf("%d\n", ans);



	return 0;
}

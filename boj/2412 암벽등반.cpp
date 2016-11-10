//2412 암벽등반

//다잌스트라  || bfs + bisearch
#include <stdio.h>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <string.h>
#include <set>
#include <map>
#include <unordered_map>
#include <functional>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9
#define MAXN			50001

int n, T;
unordered_map<LL, int> hset;
int dist[MAXN];
int bar = 10000000;
int ans = INF;
int main() {
	si(n); si(T);
	hset[0] = 0;
	for (int i = 0, a, b; i < n; i++) {
		si(a); si(b);
		hset[a*bar + b] = i + 1;
	}
	for (int i = 0; i < MAXN; i++) dist[i] = INF;
	queue <pii> q;
	q.push(pii(0, 0));	
	dist[0] = 0;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		LL xid = hset[x*bar + y];
		q.pop();
		if (y == T) 
			ans = min(ans, dist[xid]);
		
		for (int dx = -2; dx <= 2; dx++) {
			for (int dy = -2; dy <= 2; dy++) {
				int a = x + dx;
				int b = y + dy;
				LL hid = a*bar + b;
				if (hset.find(hid) == hset.end()) continue;
				int next = hset[hid];
				if (dist[next] > dist[xid] + 1) {
					dist[next] = dist[xid] + 1;
					q.push(pii(a, b));
				}
			}
		}
	}
	if (ans == INF) printf("-1\n");
	else printf("%d\n", ans);

	return 0;
}


//¿úÈ¦
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>

#define ll long long
#define pii pair<int, int>
#define si(a) scanf("%d", &(a))
#define sc(a) scanf("%c", &(a))
#define ss(a) scanf("%s",a)
#define sll(a) scanf("%lld", &(a))
#define pi(a) printf("%d\n", (a))
#define pc(a) printf("%c",a);
#define ENDL printf("\n");
#define pll(a) printf("%lld\n", (a))

#define INF 2e9
#define all(a) (a).begin(),(a).end()
#define MAX_N 501

using namespace std;
int n, m, w;
vector < pii > G[MAX_N];
int dist[MAX_N];

int main() {
	int test = 0;
	for (si(test); test > 0; test--) {
		si(n); si(m); si(w);

		vector<int> start;
		for (int i = 0; i < MAX_N; i++)
			G[i].clear();

		for (int i = 0, a, b, c; i < m; i++) {
			si(a); si(b); si(c);
			G[a].push_back(pii(b, c));
			G[b].push_back(pii(a, c));
		}
		for (int i = 0, a, b, c; i < w; i++) {
			si(a); si(b); si(c);
			G[a].push_back(pii(b, -c));
			start.push_back(a);
		}

		sort(all(start));
		start.erase(unique(all(start)), start.end());

		fill(dist, dist + MAX_N, INF);
		priority_queue<pii, vector<pii>, greater<pii> > pq;
		for (int i = 0; i < start.size(); i++) {
			pq.push(pii(0, start[i]));
			dist[start[i]] = 0;
		}
		vector<int> count(MAX_N, 0);
		int ans = false;
		while (!pq.empty()) {
			int curcost = pq.top().first;
			int cur = pq.top().second;
			pq.pop();
			if (dist[cur] < curcost) continue;

			for (int i = 0; i < G[cur].size(); i++) {
				int next = G[cur][i].first;
				int cost = G[cur][i].second;

				if (dist[next] > dist[cur] + cost) {
					count[next] += 1;
					dist[next] = dist[cur] + cost;
					if (count[next] > n) {
						ans = true;
						break;
					}
					pq.push(pii(dist[next], next));
				}
			}
			if (ans == true) break;
		}

		if (ans)printf("YES\n");
		else printf("NO\n");

	}

	return 0;
}

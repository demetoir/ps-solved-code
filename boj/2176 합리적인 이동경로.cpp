//2176 합리적인 이동경로

//다잌스트라 + dp
//거리는 최단거리라고 생각하고 풀어야한다...
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define LL				long long 
#define si(a)			scanf("%d",&(a))
#define sc(a)			scanf("%c",&(a))
#define ss(a)			scanf("%s",(a))

#define all(x)			(x).begin(),(x).end()
#define pii				pair<int, int>
#define INF				2e9

#define MAXN			1001
int n, m;
vector< pii > G[MAXN];
const int s = 1, t = 2;
vector<int> dist;

void shortpath() {
	dist = vector<int>(n + 1, INF);
	dist[t] = 0;
	queue<int>q;
	q.push(t);

	while (!q.empty()) {
		int cur = q.front(); q.pop();

		for (int i = 0; i < G[cur].size(); i++) {
			int next = G[cur][i].first;
			int cost = G[cur][i].second;
			if (dist[next] > dist[cur] + cost) {
				dist[next] = dist[cur] + cost;
				q.push(next);
			}
		}
	}
}

vector<int> memo;
int find(int cur) {
	if (memo[cur] != -1) return memo[cur];
	int ret = 0;

	for (int i = 0; i < G[cur].size(); i++) {
		int next = G[cur][i].first;
		if (dist[cur] > dist[next])
			ret += find(next);
	}

	memo[cur] = ret;
	return ret;
}
int main() {	
	si(n); si(m);
	for (int i = 0,a,b,c; i < m; i++) {
		si(a); si(b); si(c);
		G[a].push_back(pii(b, c));
		G[b].push_back(pii(a, c));
	}
	memo = vector<int>(n+1, -1);

	shortpath();
	memo[t] = 1;
	find(s);
	int ans = memo[s];
	
	printf("%d\n", ans);
	return 0;
}








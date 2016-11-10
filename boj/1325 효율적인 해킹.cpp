//1325 효율적인 해킹

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
#define MAXN			10001

int n, m;
vector<int> G[MAXN];
int check[MAXN];
int main() {
	si(n); si(m);
	for (int i = 0, a, b; i < m; i++) {
		si(a); si(b);
		G[b].push_back(a);
	}

	int ansval = -1;
	vector<int> ansL;
	for (int start = 1; start <= n; start++) {
		queue<int>q;
		q.push(start);
		memset(check, 0, sizeof(check));
		int cnt = 0;
		check[start] = 1;

		while (!q.empty()) {
			int cur = q.front(); q.pop();
			for (int j = 0; j < G[cur].size(); j++) {
				int next = G[cur][j];
				if (check[next]) continue;
				check[next] = 1;
				cnt++;
				q.push(next);
			}
		}

		ansL.push_back(cnt);
		if (ansval < cnt) ansval = cnt;		
	}

	for (int i = 0; i < n; i++)
		if(ansval == ansL[i])
			printf("%d ", i+1);
	printf("\n");

	return 0;
}







//11286 절대값 힙

//pq 응용
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
int n;

int ans;
priority_queue<pii, vector<pii>, greater<pii> > pq;
int main() {
	si(n);
	for (int i = 0,a; i < n; i++) {
		si(a);
		if (a) {
			if (a > 0)pq.push(pii(a, 1));
			else pq.push(pii(-a, -1));
		}
		else {		
			if (pq.empty())printf("0\n");
			else {
				printf("%d\n", pq.top().second*pq.top().first);
				pq.pop();
			}
		}
	}
	return 0;
}


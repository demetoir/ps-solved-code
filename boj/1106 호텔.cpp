//1106 È£ÅÚ

//³À»ö dp
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <math.h>
using namespace std;


#pragma warning(disable:4996)
#define LL				long long 
#define pii				pair<int, int>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define sLL(a)			scanf("%lld", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAXN			100001
#define pb(a)			push_back((a))
int n, c;
vector<pii>v;
vector<int> dp, dp2;
int gcd(int a, int b){
	if (a < b) swap(a, b);
	if (b == 0) return a;
	return gcd(b, a%b);	
}

int ans = INF;
int cost[123];
int p[123];
int main() {
	si(c);si(n);
	for (int i = 0,a,b; i < n; i++) {
		si(a);si(b);		
		//cost[i] = a/gcd(a, b);
		//p[i] = b/gcd(a, b);
		cost[i] = a;
		p[i] = b;
	}

	dp.assign(2000, INF);
	dp[0] = 0;
	for (int iter = 0; iter < n; iter++) {
		for (int i = p[iter]; i < 2000; i++) {
			dp[i] = min(dp[i], dp[i - p[iter]] + cost[iter]);
		}
	}

	for (int i = c; i < 2000; i++) 
		ans = min(dp[i], ans);

	printf("%d\n", ans);
	return 0;
}

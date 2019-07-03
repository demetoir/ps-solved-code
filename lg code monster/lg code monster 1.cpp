
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
#define sLL(a)			scanf("%lld", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N			10001
#define pb(a)			push_back((a))

LL ans;
LL a, b;
int main() {
	int test;
	for (si(test); test > 0; test--) {
		sLL(a); sLL(b);
		LL A = 0, B = 0;
		while (a) {
			A += a;
			a /= 2;
		}
		while (b) {
			A += b;
			b /= 2;
		}
		ans = B-A;
		printf("%d"\n)'
	}



	return 0;
}

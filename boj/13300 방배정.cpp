//13300 πÊπË¡§

#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
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

int n, k;
int A[7];
int B[7];
int main() {
	si(n); si(k);
	for (int i = 0,a,b; i < n; i++) {
		si(a); si(b);
		if (a == 0)A[b] ++;
		else B[b] ++;
	}
	int ans = 0;
	for (int i = 1; i <= 6; i++) {
		ans += A[i] / k+B[i]/k;
		if (A[i] % k) ans++;
		if (B[i] % k) ans++;
	}
	printf("%d\n",ans);
	return 0;
}

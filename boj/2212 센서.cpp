//2212 센서

//아이디어
//dp가 아니다 아이디어다
//양쪽 끝점에서 서로다른 감지국 사이의 가장 먼 센서 끼리의 거리차를 생각하는게 중요
//각 거리차중에서 가장 큰 놈들고르면 된다
//
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <functional>
#include <stdio.h>
#include <deque>
using namespace std;

#define LL				long long 
#define pii				pair<int, int>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define ss(a)           scanf("%s", (a))
#define all(a)			(a).begin() , (a).end()
#define INF             2e9
#define LLINF			1e17
#define MAX_N			10001


int n, m, k;
vector<int> A,v;
int main() {
	si(n);si(k);
	for (int i = 0,val; i < n; i++) {
		si(val);
		A.push_back(val);
	}

	sort(all(A));
	LL res = A[n - 1] - A[0];
	for (int i = 1; i < n; i++) 
		v.push_back(A[i] - A[i - 1]);

	sort(all(v));
	for (int i = 0; i < k - 1 &&  i<n-1; i++) {
		res -= v[ n -i -2];
	}
	printf("%lld\n",res);
	
	return 0;
}

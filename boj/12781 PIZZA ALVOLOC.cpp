
//12781 PIZZA ALVOLOC


//기하 기초 선분 교차판별

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>
using namespace std;

typedef long long LL;
#define pii pair<int, int>
#define si(a) scanf("%d", &(a))
#define sc(a) scanf("%c", &(a))
#define ss(a) scanf("%s",a)
#define sLL(a) scanf("%lld", &(a))
#define pi(a) printf("%d\n", (a))
#define pc(a) printf("%c",a);
#define ENDL printf("\n");
#define pll(a) printf("%lld\n", (a))

#define INF 2e9
#define LLINF 1e16
#define all(a) (a).begin(), (a).end()
#define MAX_N 51
int ans;
int a, b, c, d;
int x,y,z,w;

double ccw(int a, int b, int c, int d, int e, int f) {
	int ax = a - c;
	int ay = b - d;
	int bx = a - e;
	int by = b - f;
	return ax * by - bx * ay;
}

//bool segmentIntersection(vector2 a, vector2 b, vector2 c, vector2 d) {
//	double ab = ccw(a, b, c) * ccw(a, b, d);
//	double cd = ccw(c, d, a) * ccw(c, d, b);
//
//	if (ab == 0 && cd == 0) {
//		if (b < a)swap(a, b);
//		if (d < c) swap(c, d);
//		return !(b< c || d < a);
//	}
//	return ab <= 0 && cd <= 0;
//}

int main() {
	si(a);	si(b);	si(c);	si(d);
	si(x);	si(y);	si(z);	si(w);
	double A = ccw(a, b, c, d, x, y) * ccw(a, b, c, d, z, w);
	double B = ccw(x, y, z, w, a, b) * ccw(x, y, z, w, c, d);

	ans = 0;
	if (A == 0 && B == 0) {
		ans = 0;
	}
	if (A <= 0 && B <= 0)ans = 1;
	printf("%d\n", ans);
	return 0;
}
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

int n = 0;
double x[MAXN];
double up[MAXN];
double down[MAXN];
double mid[MAXN];
double ans;
double getD(double c, double d, double a, double b) {
	double val = sqrt((c - a)*(c - a) + (d - b)*(d - b));
	return val;
}

double ismove(int idx) {
	double curval = 0;
	if (idx > 0)
		curval += getD(x[idx - 1], mid[idx - 1], x[idx], mid[idx]);
	if (idx + 1 < n)
		curval += getD(x[idx], mid[idx], x[idx + 1], mid[idx + 1]);

	if (fabs(curval - up[idx]) < 1e-4)return 0;
	if (fabs(curval - down[idx]) < 1e-4)return 0;
	double lo, hi;
	//lower
	lo = mid[idx];

	hi = up[idx];
	double upperval = curval;
	double uppery = 0;
	if (fabs(hi - lo) > 1e-4) {
		for (int cnt = 0; cnt < 100; cnt++) {
			double midval = (hi + lo) / 2;
			double val = 0;
			if (idx > 0)
				val += getD(x[idx - 1], mid[idx - 1], x[idx], midval);
			if (idx + 1 < n)
				val += getD(x[idx], midval, x[idx + 1], mid[idx + 1]);

			if (upperval > val) {
				upperval = val;
				uppery = midval;
				lo = midval;
			}
			else
				hi = midval;
		}
	}
	//upper
	hi = mid[idx];
	lo = down[idx];
	double lowerval = curval;
	double lowery = 0;
	if (fabs(hi - lo) > 1e-4) {
		for (int cnt = 0; cnt < 100; cnt++) {
			double midval = (hi + lo) / 2;
			double val = 0;
			if (idx > 0)
				val += getD(x[idx - 1], mid[idx - 1], x[idx], midval);
			if (idx + 1 < n)
				val += getD(x[idx], midval, x[idx + 1], mid[idx + 1]);

			if (lowerval > val) {
				lowerval = val;
				lowery = midval;
				hi = midval;
			}
			else {
				lo = midval;
			}
		}
	}
	if (upperval < lowerval)
		return uppery;

	if (upperval > lowerval)
		return lowery;

	return 0;
}
int main() {
	int test;
	for (si(test); test > 0; test--) {
		si(n);
		for (int i = 0, a, b, c; i < n; i++) {
			si(a); si(b); si(c);
			x[i] = a;
			down[i] = b;
			up[i] = c;
		}

		for (int i = 0; i < n; i++) {
			mid[i] = (double)(down[i] + up[i]) / 2.0;
		}

		double preval = 0;
		for (int i = 0; i < n - 1; i++)
			preval += getD(x[i], mid[i], x[i + 1], mid[i + 1]);

		while (1) {
			bool flag = false;
			for (int i = 0; i < n; i++) {
				double newval = ismove(i);
				if (newval == 0) continue;
				mid[i] = newval;
				flag = true;
			}
			if (flag == false)
				break;

			double curval = 0;
			for (int i = 0; i < n - 1; i++)
				curval += getD(x[i], mid[i], x[i + 1], mid[i + 1]);
			printf("%###lf %lf\n", preval, curval);
			if (fabs(preval - curval) < 1e-4)
				break;
			preval = curval;
		}

		ans = 0;
		for (int i = 0; i < n - 1; i++) {
			ans += getD(x[i], mid[i], x[i + 1], mid[i + 1]);
		}

		printf("%.2lf\n", ans);

	}
	return 0;
}

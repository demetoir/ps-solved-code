//codeforce 733d

#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <string.h>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9


struct S {
	int a, b, c, n;
	S() {};
	S(int a, int b, int c, int n) :a(a), b(b), c(c), n(n) {};
};

vector<S> v;
bool cmp(const S &x, const S &y) {
	if (x.a != y.a) return x.a < y.a;
	if (x.b != y.b) return x.b < y.b;
	return x.c < y.c;
}

bool cmp2(S &x, S &y) {
	return x.n == y.n;
}
int n;
int ansa, ansb = -1;
double ansval = 0;

void input() {
	si(n);
	for (int i = 0; i < n; i++) {
		int a, b, c;
		si(a);
		si(b);
		si(c);
		double val = (double) min(min(a, b), c) / 2.0;
		if (val > ansval) {
			ansval = val;
			ansa = i + 1;
		}
		
		v.push_back(S(a, b, c, i + 1));
		v.push_back(S(a, c, b, i + 1));
		v.push_back(S(b, a, c, i + 1));
		v.push_back(S(b, c, a, i + 1));
		v.push_back(S(c, a, b, i + 1));
		v.push_back(S(c, b, a, i + 1));
	}
}
int main() {
	input();
	sort(all(v), cmp);
	for (int i = 0; i < v.size() - 1; i++) {
		//printf("%d\n",i);
		for (int j = i+1; j < v.size(); j++) {
			if (v[i].n == v[j].n) continue;
			if (v[i].a == v[j].a && v[i].b == v[j].b) {
				double val = v[i].c + v[j].c;
				if (val > v[i].a) val = v[i].a;
				if (val > v[i].b) val = v[i].b;
				val /= 2.0;
				if (val > ansval) {
					ansval = val;
					ansa = v[i].n;
					ansb = v[j].n;
				}
			}
			break;
		}
	}

	if (ansb != -1) 
		printf("2\n%d %d\n", ansa, ansb);
	else 
		printf("1\n%d\n", ansa);
	

	return 0;
}



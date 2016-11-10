//2300 기지국
//2차원 dp 
//n^2 라서 10000에는 안풀릴것같은데 맞았다... why?
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9
int n;
vector<pii> cord;
int memo[12345];
struct S {
	int x, y, n;
	S(int x, int y, int n) : x(x), y(y), n(n) {};
	S() {};
};
int main() {

	si(n);
	cord.push_back(pii(-INF, 0));
	for (int i = 0,a,b; i < n; i++) {
		si(a); si(b);
		cord.push_back(pii(a, abs(b)));
	}
	sort(all(cord));
	int ans = 0;

	memset(memo, -1, sizeof(memo));
	memo[0] = 0;
	sort(all(cord));

	//(y,num)
	vector<S> stk;
	for (int i = 1; i <= n; i++) {
		int x = cord[i].first;
		int y = cord[i].second;
		int ret = INF;

		while (!stk.empty()) {
			if (stk.front().y > y)break;
			stk.pop_back();
		}
		stk.push_back(S(x,y,i));
		
		
		for (int j = i; j >=1 ; j--) {
			int num = j;
			int dx = x - cord[j].first;
			y = max(y, cord[j].second);
			ret = min(ret, memo[num - 1] + max(y*2,dx));
		}
		memo[i] = ret;
	}

	ans = memo[n];
	printf("%d\n", ans);
	return 0;
}
// 7579 앱

//dp 냅색 응용 + 아이디어
//다시 볼문제
//처음에는 그리디로 했다가 틀림
//그래서 dp 냅색 으로 푼다
//메모리를 인자로 잡으면 너무 커서 안되므로
//비용을 인자로 잡는다
//단순히 넣냐 안넣냐로 생각하는걸 먼저 떠올려야겟다
//이거를 재귀로 짜는거를 dp로 옮기면된다
//윈도우 슬라이딩 기법을 쓰는 동안 i번쨰를 하는데 그전으로 나오지 않는 용량은 
//넘어가는 거를 고려해야한다
//i번째를 넣을떄가 처음일때는 따로 처리한다

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>
#include <limits.h>

typedef long long LL;
using namespace std;

#define pii pair<int, int>
#define PLL pair<LL,LL>
#define si(a) scanf("%d", &(a))
#define sc(a) scanf("%c", &(a))
#define ss(a) scanf("%s",a)
#define sll(a) scanf("%lld", &(a))
#define pi(a) printf("%d\n", (a))
#define pc(a) printf("%c",a);
#define ENDL printf("\n");
#define pll(a) printf("%lld\n", (a))
#define INF 2e9
#define LLINF 1e17 
#define all(a) (a).begin(),(a).end()

#define MAX_N 101l

LL memory[MAX_N];
LL cost[MAX_N];
LL n, m;
LL ans;

int main() {
	sll(n);
	sll(m);

	for (LL i = 0, val; i < n; i++) sll(memory[i]);
	for (LL i = 0, val; i < n; i++) sll(cost[i]);

	vector<LL> dp1(10001,0);
	for (int i = 0; i < n; i++) {
		vector<LL> dp2 = dp1;

		dp2[cost[i]] = max(dp2[cost[i]], memory[i]);
		for (int j = 0; j < 10001; j++) {
			if (dp1[j] == 0) continue;
			if (j + cost[i] > 10000) break;
			dp2[j + cost[i]] = max(dp2[j +cost[i]] , dp1[j] + memory[i]);
		}
		dp1 = dp2;
	}

	for (int i = 0; i < 10001; i++) {
		if (dp1[i] >= m) {
			ans = i;
			break;
		}
	}

	pll(ans);
	return 0;
}

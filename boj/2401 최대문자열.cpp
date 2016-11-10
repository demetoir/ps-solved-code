//2401 최대문자열

//kmp + dp
//hey 에서 패턴들이 나타나는 위치를 찾고 각 시작위치마다 매칭되는 패턴의 길이를 저장한다
//그러면 막대기에서 부분부분별로 덮는 dp 가되는데
//여기서 가장 길게 붙여놓는거는 매칭되는 패턴이 서로 겹치지 않고 연속 되지 않아도 될때
//가장만히 덮을때의 최대값을 구하는것이다
//연속 되는줄 알고 헤멨다
//dp는 현재 점에서 덮을때와 안덮을때 두가지로 나누어서 풀면된다
//포도주 시식이랑 비슷하다

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

typedef long long ll;
#define pii pair<int, int>
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

#define MAX_N 501

using namespace std;


ll n;
vector<int> G[100001];
string hey;
char buff[100001];

vector<char> make_pie(string str) {
	ll n = str.size();
	vector<char> pie(n);

	ll start = 1, match = 0;
	while (start + match < n) {
		if (str[start + match] == str[match]) {
			match++;
			pie[start + match - 1] = match;
		}
		else {
			if (match == 0)start++;
			else {
				start += match - pie[match - 1];
				match = pie[match - 1];
			}
		}
	}
	return pie;
}

void kmp(string &hey, string &pattern) {
	int h = hey.size();
	int n = pattern.size();

	vector<char> pie = make_pie(pattern);
	ll start = 0, match = 0;

	while (start <= h - n) {
		if (hey[start + match] == pattern[match]
			&& match < n) {

			match++;
			if (match == n) 			
				G[start].push_back(n);
			
		}
		else {
			if (match == 0) start += 1;
			else {
				start += match - pie[match - 1];
				match = pie[match - 1];
			}
		}
	}

	return;
}

int dp1[100001];
int dp2[100001];
int main() {
	ss(buff);
	hey = string(buff);
	sll(n);
	for (int i = 0; i < n; i++) {
		ss(buff);
		string str(buff);
		kmp(hey, str);

	}

	int h = hey.size();
	int ans = 0;


	dp1[h] = dp2[h] = 0;
	for (int i = h - 1; i >= 0; i--) {
		dp1[i] = 0;
		for (int j = 0; j < G[i].size(); j++) {
			int len = G[i][j];
			dp1[i] = max(dp1[i], len + dp1[i + len]);
			dp1[i] = max(dp1[i], len + dp2[i + len]);
		}

		dp2[i] = max(dp2[i], dp2[i + 1]);
		dp2[i] = max(dp2[i], dp1[i + 1]);
		ans = max(dp1[i], ans);
		ans = max(dp2[i], ans);
	}


	printf("%d", ans);
	return 0;
}

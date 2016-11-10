//9996 한국이 그리울 땐 서버에 접속하지
//
//2차원 ,3상태 , dp
//* 는 비어있을때 을 잘고려해야한다
//

#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;
typedef pair<int, int> pii;
typedef long long LL;
#define si(a)			scanf("%d",&(a))
#define sc(a)			scanf("%c",&(a))
#define ss(a)			scanf("%s",(a))

#define all(x)			(x).begin(), (x).end()
#define INF				2e9
#define MAXN			1001

char pattern[123];
char str[123];
int n,a,b;
int dp[123][123];
//x - parttern, y = str
int f(int x, int y) {
	if (x == 0 && y == 0) return 1;
	if (x == -1 || y == -1) return 0;

	if (dp[x][y] != -1) return dp[x][y];
	int ret = 0;
	if (pattern[x-1] == '*') {
		for (int i = -1; i <= y; i++)
			ret = max(ret, f(x - 1, i));		
	}
	else {
		if (pattern[x-1] == str[y-1]) 
			ret = max(ret, f(x-1,y-1));
	}
	dp[x][y] = ret;
	return ret;
}
int main() {	

	si(n);
	ss(pattern);
	a = strlen(pattern);
	for (int i = 0; i < n; i++) {
		ss(str);
		b = strlen(str);
		for (int j = 0; j < 123; j++)
			for (int k = 0; k < 123; k++)
				dp[j][k] = -1;
		
		int ans = f(a, b);

		if (ans) printf("DA\n");
		else printf("NE\n");
	}
	return 0;
}








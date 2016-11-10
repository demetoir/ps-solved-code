//2186 ¹®ÀÚÆÇ

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
#define LL              long long 
#define pii             pair<long long, long long>
#define si(a)           scanf("%d", &(a))
#define sc(a)           scanf("%c", &(a))
#define sll(a)          scanf("%lld", &(a))
#define ss(a)           scanf("%s", (a))

#define INF             2e9
#define LLINF			1e17
#define MAX_N 123456

int n, m, k;
char grid[123][123];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

int main() {
	si(n);
	si(m);
	si(k);
	for (int i = 0; i < n; i++) {
		char str[123];
		ss(str);
		for (int j = 0; j < m; j++) {
			grid[i][j] = str[j];
		}
	}

	vector< vector<int> > dp1,dp2;
	dp1.assign(123, vector<int>(123,0));
	char str[123];
	ss(str);
	int size = strlen(str);	


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (grid[i][j] == str[0])
				dp1[i][j] = 1;
		}
	}

	for (int idx = 1; idx < size; idx++) {
		dp2.assign(123, vector<int>(123, 0));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				//if (grid[i][j] != str[idx - 1])  continue;

				for (int d = 0; d < 4; d++) {
					for (int mul = 1; mul <= k; mul++) {
						int a = i + mul*dx[d];
						int b = j + mul*dy[d];
						if (a < 0 || a >= n || b < 0 || b >= m)continue;
						if (grid[a][b] == str[idx])
							dp2[a][b] += dp1[i][j];
					}
				}
			}
		}
		dp1 = dp2;
	}

	int ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			//if(grid[i][j] == str[size-1])
			ans += dp1[i][j];
		}
	}

	printf("%d\n", ans);
	return 0;
}
//2251 물통
//시뮬레이션 그래프 탐색
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define LL				long long 
#define si(a)			scanf("%d",&(a))
#define sc(a)			scanf("%c",&(a))
#define ss(a)			scanf("%s",(a))

#define all(x)			(x).begin(),(x).end()
#define pii				pair<int, int>
#define INF				2e9

#define MAXN			1001

int n,ans;
int m[3];
int check[432];
int memo[201][201][201];
int dx[6] = { 0,0,1,1,2,2 };
int dy[6] = { 1,2,0,2,0,1 };
void f(int buck[3]) {
	int x = buck[0];
	int y = buck[1];
	int z = buck[2];
	if (memo[x][y][z])return;
	memo[x][y][z] = 1;

	if( x ==0 )
		check[z] = 1;

	int newbuck[3];
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 3; j++)newbuck[j] = buck[j];
		int x = buck[dx[i]], y = buck[dy[i]];
		if (x + y > m[dy[i]]) {
			x = x + y - m[dy[i]];
			y = m[dy[i]];
		}
		else {
			y = x + y;
			x = 0;
		}
		newbuck[dx[i]] = x;
		newbuck[dy[i]] = y;
		f(newbuck);
	}
	return;
}


int start[3];
int main() {	
	si(m[0]);si(m[1]);si(m[2]);
	start[2] = m[2];
	f(start);
	
	for (int i = 0; i < 201; i++) 
		if (check[i])
			printf("%d ",i);
	printf("\n");

	return 0;
}








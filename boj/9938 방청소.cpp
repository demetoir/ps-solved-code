//9938 방청소

//union find 
//http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220791837179
//답보고 풀었다...
//
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <string.h>
#include <set>
#include <map>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9
#define MAXN			300010

int N, L;
int A[MAXN], B[MAXN];
int p[MAXN];
int check[MAXN];
int find(int a) {
	if (p[a] == a) return a;
	return p[a] = find(p[a]);
}

bool unite(int x, int y) {
	int a = find(x);
	int b = find(y);

	if (a == b) return false;

	p[b] = a;
	return true;
}
int main() {
	for (int i = 0; i < MAXN; i++) p[i] = i;

	si(N); si(L);	
	int last = L + 1;
	for (int i = 0,a,b; i < N; i++) {
		si(a); si(b);
		if (check[a] == 0) {
			check[a] = 1;
			unite(b, a);
		}
		else if (check[b] == 0) {
			check[b] = 1;
			unite(a, b);
		}
		else if (check[find(a)] == 0) {
			check[find(a)] = 1;
			unite(find(b), find(a));
		}
		else if (check[find(b)] == 0) {
			check[find(b)] = 1;
			unite(find(a), find(b));
		}
		else {
			printf("SMECE\n");
			continue;
		}
		printf("LADICA\n");
	}

	return 0;
}

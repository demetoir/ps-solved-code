//4195 模备 匙飘况农

// union find 览侩
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
#define MAXN			100000
int n;
int parent[123456];
int level[123456];
int number[123456];
map<string, int> nameset;
int find(int x) {
	if (parent[x] == x)return x;
	return parent[x] = find(parent[x]);
}
void unite(int x , int y) {
	int a = find(x);
	int b = find(y);
	if (a == b)return ;

	if (level[a] == level[b]) {
		level[a] ++;
		number[a] += number[b];
		parent[b] = a;
	}
	else if (level[a] > level[b]) {
		parent[b] = a;
		number[a] += number[b];
	}
	else {
		parent[a] = b;
		number[b] += number[a];
	}
}
int getsize(int a) {
	return number[find(a)];
}

int main() {
	int test; si(test);
	for (; test > 0; test--) {
		nameset.clear();
		for (int i = 0; i < MAXN; i++) {
			level[i] = 0;
			parent[i] = i;
			number[i] = 1;
		}

		si(n);
		int setsize = 0;
		for (int i = 0; i < n; i++) {
			char a[32], b[32];
			ss(a); ss(b);
			string x(a), y(b);
			if (nameset.find(x) == nameset.end()) {
				nameset[x] = setsize;
				setsize++;
			}
			if (nameset.find(y) == nameset.end()){
				nameset[y] = setsize;
				setsize++;
			}

			unite(nameset[x], nameset[y]);
			int ans = getsize(nameset[x]);
			printf("%d\n", ans);
		}
	}
	return 0;
}



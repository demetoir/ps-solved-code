// 5419 북서풍
// 인덱스트리,인덱스트리 좌표 압축, 이분탐색, 좌표 정렬, 아이디어
// 인덱스트리를 응용하는 문제이다
// x축으로 작고 y축으로는 큰 순서대로 정렬하고
// 왼쪽 아래서 점부투 시작하면서 yset에서 인덱스 트리로 현재 위치보다 아래인것을 고른다
// 그리고 yset에 지금 좌표를 추가하고 다음걸로 넘어감
// yset에는 지금까지 검사 한점들을 정렬된 순서대로 놓는다
// 이때 범위가 크기 떄문에 좌표 압축을 해야한다
// long long 에서 틀렷다...
// 그냥 다음에는 다 롱롱 쓰자
//참고 자료
//http://www.roman10.net/2012/03/16/suffix-array-part-3-longest-common-substring-lcs/

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;
#define LL long long
#define si(a) scanf("%d",&(a))
#define ss(a) scanf("%s"&(s))
#define pii pair<int,int>
#define pLL pair<LL,LL>
#define INF 2e9
#define MAX_N 1000000
#define all(a) (a).begin(), (a).end()
int n;
vector<pLL> A;
vector<int> dp;
vector<int> yset;
LL ans;
bool cmp(pLL A, pLL B) {
	if (A.first != B.first) return A.first > B.first;
	return A.second < B.second;
}
int tree[MAX_N];
void update(int index, int diff) {
	while (index < MAX_N) {
		tree[index] += diff;
		index += (index& -index);
	}
}
int get(int index) {
	int ret = 0;
	while (index > 0) {
		ret += tree[index];
		index -= (index & -index);
	}
	return ret;
}



int main() {
	int test;
	si(test);
	for (; test > 0; test--) {
		si(n);
		A.clear();
		ans = 0;
		dp.assign(n,1);
		yset.clear();
		memset(tree, 0, sizeof(tree));
		for (int i = 0, a, b; i < n; i++) {
			si(a); si(b);
			A.push_back(pLL(a, b));
			yset.push_back(b);
		}
		sort(all(A), cmp);

		sort(all(yset));
		ypoll.erase(unique(all(yset)), yset.end());

		for (int i = 0; i < n; i++) {
			int a = A[i].first, b = A[i].second;
			int index = lower_bound(all(yset), b) - yset.begin() +1;
			ans += get(index);
			int val = get(index);
			update(index, 1);
		}
		printf("%lld\n", ans);
	}
	return 0;
}

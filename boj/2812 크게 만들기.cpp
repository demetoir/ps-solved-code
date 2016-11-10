//2812 크게 만들기

//게시판에서 테스트 케이스를 보고 풀었다
//앞에서부터 k개 지울수 있을때 지우 않을 수있 놈은 K+1가지 존재함
//앞에서 k+1개 중 가장 크고 먼저 나오는것(val)만 남기고 앞의 것은 제거함
//가장 크고 먼저나오는것은 숫자가 0~9이므로 가장 각각 숫자마다 의 인덱스를 정렬한 
//다음 lower bound 로 찾는다
//지운 갯수만큼 k 줄이고
//가장 앞을 나타내는 포인터 l을 val +1로 옮긴다


#include <cstdio>
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
#define MAXN			500010

int N, K;
char num[MAXN];
int check[MAXN];
vector<int> idx[12];

int main() {
	si(N); si(K);
	ss(num);
	for (int i = 0; i < N; i++) idx [num[i] - '0'].push_back(i);
	
	for (int i = 0; i < 10; i++) sort(all(idx[i]));
	
	int l = 0;
	int k = K;
	
	while (k>0){
		for (int i = 9; i >= 0; i--) {
			if (lower_bound(all(idx[i]), l) == idx[i].end()) continue;
			int val = idx[i][ lower_bound(all(idx[i]), l) - idx[i].begin() ];
			if (val > l + k) continue;

			check[val] = 1;
			k -= val - l ;
			l = val + 1;
			break;
		}
	}
	
	for (int i=0; i < N; i++) {
		if (check[i] || i >=l )printf("%c", num[i]);
	}
	printf("\n");
	return 0;
}

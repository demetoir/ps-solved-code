//2209 버스 터미널

//minimum diameter spanning tree 
//최소 지름 신장 트리 중 이항트리일때 최소 지름을 구하는 문제
//더 빠르게 풀수있다
//
//n^3 풀이
//n == 2일때는 따로 처리
//중심 h1,h2가 될수 있는 모든 쌍에대하여 검사한다.
//
//중심지가 아닌 모든 정류장은 h1 또는 h2에 인접해야한다.
//-> 두집합으로 나눌수있다
//트리의 지름이 되는 경우는 양끝 노드가 a,b 일떄 
//	a <-> h1 <-> b
//	a <-> h1 <-> h2 <-> b

// 두가지 경우가 존재한다
// 노드들을 h1 와 인접한 노드의 집합을 A, h2와 인접한 노드들의 집합을 B라고 부르자.
// 고정된 h1,h2에 대하여 각각 집합에서 가장 큰것과 두번째로 큰것
// 그리고 각각의 집합에서 가장 큰것과 h1 ~ h2 까지의 거리 중 가장 큰것
// 이 3가지 중 가장 큰 값이 두집합으로 나누었을때의 지름이다.
// 우리가 관심있는것은 각집합에서 가장 큰것과 두번째로 큰것이다.
// 집합 A에서 가장 큰 값을 가지는 노드를 제외한 노드들을 집합 B로 이동시키지 않는것이
// 이동 시키는 것보다 이득을 본다
// 넘어간다면 집합B에서 이동시킨 노드가 가장 큰값또는 두번째로 큰값보다 크다면 지름이 더 커진다
// 따라서 A집합에서 가장 큰값을 B집합으로 하나씩 보내면서 지름을 검사하면 된다

// A집합이 가질수있는 최대값과 두번째 최대값은 정해져있음
// B집합의 최대값과 두번째 최대값을 가장 작게 만들려먼 A집합에서 최대로 가지는것이 이득이다


#include <stdio.h>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <string.h>
#include <set>
#include <map>
#include <functional>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define ss(a)			scanf("%s",(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9
#define MAXN			501

int n;
int A[MAXN], B[MAXN];
int dist[MAXN][MAXN];
vector< pii > di[MAXN];

int ans = INF;
int st1[1000];
int st2[1000];
int vi[1000];
int main() {
	si(n);
	for (int i = 0; i < n; i++) {
		si(A[i]);	si(B[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			dist[i][j] = abs(A[i] - A[j]) + abs(B[i] - B[j]);
			di[i].push_back(pii(dist[i][j], j));
		}
	}

	for (int i = 0; i < n; i++) {
		sort(all(di[i]));
	}

	ans = INF;
	if (n == 2) {
		ans = dist[0][1];
		printf("%d\n", ans);
		return 0;
	}
	for (int a = 0; a < n; a++) {
		for (int b = a + 1; b < n; b++) {
			if (a == b) continue;

			//st 는 단조 증가함
			int sti1 = 0;
			int sti2 = 0;
			int mid = dist[a][b];
			int val = INF;

			int visize = 0;
			//a,b는 제외
			for (int i = 0; i < n; i++) {
				if (di[a][i].second == a || di[a][i].second == b) continue;
				vi[visize++] = i;

			}

			for (int j = visize; j >= 0; j--) {
				int i = vi[j];
				if (di[a][i].second == a || di[a][i].second == b) continue;
				int ma1 = 0, ma2 = 0, mb1 = 0, mb2 = 0, temp = 0;

				ma1 = di[a][i].first;
				if (j >= 1) ma2 = di[a][vi[j - 1]].first;

				// cal mb1,mb2
				mb1 = st1[sti1];
				mb2 = st2[sti2];

				temp = max(temp, ma1 + ma2);
				temp = max(temp, mb1 + mb2);
				temp = max(temp, ma1 + mid + mb1);
				val = min(val, temp);
				//printf("%d : %d <= %d %d : %d %d : %d\n", i, temp, ma1,ma2, mb1,mb2, mid);

				// cal st1,st2
				int idx = di[a][i].second;
				int topval = dist[b][idx];
				if (topval >= st1[sti1]) {
					sti2++;
					st2[sti2] = st1[sti1];
					sti1++;
					st1[sti1] = topval;
				}
				else if (topval >= st2[sti2]) {
					sti2++;
					st2[sti2] = topval;
				}

			}
			//printf("## %d %d  : %d \n", a + 1, b + 1, val);
			ans = min(ans, val);
		}
	}

	printf("%d\n", ans);
	return 0;
}


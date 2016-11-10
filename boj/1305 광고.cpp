//1305 광고
//
//kmp 
//반복되는것중 가장 작은 길이 를 찾는 문제
//광고가 반복되기때문에 처음부터 길이 만큼 반복하고 끝에 광고 앞부분 만 남게 된다
//처음에는 sa 로 접근함
//근데 틀림
//kmp로 바꾸어서 보니 kmp 에서 pie를 만드는 부분이 답이된다
//pie[i]== i번쨰 까지 매칭됬을때 가장 긴 놈의 길이, 접두사와 접미사 같을때 가장 긴 길이
//따라서 n - pie[n-1] 전체 길이에서 접두사와 접미사 가 같은 놈들중 가장 긴놈을 뺀것이 답이됨
//sa는 아마 바로 앞에있는거만해서 틀린하다 정확히는 모름

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
#include <functional>
#include <utility>

#define ll long long
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
#define all(a) (a).begin(),(a).end()
#define MAX_N 1000001

using namespace std;

vector<int> make_pie(string &str) {
	int n = str.size();
	vector <int> pie(n);

	int start = 1;
	int match = 0;
	while (start + match < n) {
		if (str[start + match] == str[match]) {
			match++;
			pie[start + match - 1] = match;
		}
		else {
			if (match == 0) start++;
			else {
				start += match - pie[match - 1];
				match = pie[match - 1];
			}
		}
	}
	return pie;

}

char buff[MAX_N];
int n;
int main() {
	si(n);
	ss(buff);
	if (n == 1) {
		printf("1\n");
		return 0;
	}
	string str(buff);
	vector<int>pie;
	pie = make_pie(str);
	int ans = n - pie[n - 1];

	printf("%d\n", ans);
	return 0;
}

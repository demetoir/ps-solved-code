////10266 시계사진들
//
////kmp 응용
////모델링 문제
////원형 문자열에서 패턴을 찾는 문제
////일단 a,b 둘다 소트
////원형 문자열이므로 a는 a+a함
////여기서 문자가 되는것은 각 인접한 바늘의 각도 차이 가 되므로
////인접한 바늘끼리의 각도 차를 만든다
////그러면 문자열 a 에서 패턴 b를 찾는 문제가 된다
//
//
//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <functional>
//#include <utility>
//
//typedef long long ll;
//#define pii pair<int, int>
//#define si(a) scanf("%d", &(a))
//#define sc(a) scanf("%c", &(a))
//#define ss(a) scanf("%s",a)
//#define sll(a) scanf("%lld", &(a))
//#define pi(a) printf("%d\n", (a))
//#define pc(a) printf("%c",a);
//#define ENDL printf("\n");
//#define pll(a) printf("%lld\n", (a))
//
//#define INF 2e9
//#define all(a) (a).begin(),(a).end()
//#define MAX_N 1000001
//
//using namespace std;
//
//#define MOD 360000
//
//char buff[MAX_N];
//ll n;
//ll A[MAX_N],B[MAX_N];
//
//vector <ll>pie;
//vector <ll> pattern, hey;
//
//
//vector<ll> make_pie(vector<ll>str){
//	ll n = str.size();
//	vector<ll> pie(n);
//	ll start = 1, match = 0;
//
//	while (start + match < n) {
//		if (str[start + match] == str[match]) {
//			match++;
//			pie[start + match - 1] = match;
//		}
//		else {
//			if (match == 0)start++;
//			else {
//				start += match - pie[match - 1];
//				match = pie[match - 1];
//			}
//		}
//	}
//	return pie;
//}
//
//bool kmp() {
//	int h = hey.size();
//	int n = pattern.size();
//	ll start = 0, match = 0;
//
//	while (start <= h-n) {
//		if (hey[start + match] == pattern[match]
//			&& match < n) {
//
//			match++;
//			if (match == n)return true;
//		}
//		else {
//			if (match == 0) start += 1;
//			else {
//				start += match - pie[match - 1];
//				match = pie[match - 1];
//			}
//		}
//	}
//
//	return false;
//}
//
//int main() {	
//	sll(n);
//	for (ll i = 0; i < n; i++) sll(A[i]);
//	for (ll i = 0; i < n; i++) sll(B[i]);
//	sort(A, A + n);
//	sort(B, B + n);
//
//	for (int i = 0; i < n; i++) A[i + n] = A[i];
//
//	for (int i = 0 ; i< n*2-1; i++) 
//		hey.push_back( (A[i+1] - A[i]+MOD)%MOD );
//	
//	for (int i = 0; i < n-1; i++)
//		pattern.push_back(B[i + 1] - B[i]);
//
//	pie = make_pie(pattern);
//	
//
//	if (kmp())
//		printf("possible\n");
//	else
//		printf("impossible\n");
//
//	return 0;
//}

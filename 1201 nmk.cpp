////1201 nmk
//
////답보고 풀엇다...
////수학... 그리디는 개뿔
//
//#include <iostream>
//#include <stdio.h>
//#include <vector>
//#include <queue>
//#include <algorithm>
//using namespace std;
//
//
//#define LL				long long 
//#define si(a)			scanf("%d",&(a))
//#define ss(a)			scanf("%s",(a))
//#define all(x)			(x).begin(),(x).end()
//
//int n,m,k;
//int A[4321];
//int main() {
//	si(n);	si(m); si(k);
//	if (n < m + k -1 || n > m*k) {
//		printf("-1\n");
//		return 0;
//	}
//	for (int i = 0; i < n; i++) A[i] = i + 1;
//
//	priority_queue<int>q;
//	for (int i = 0; i < (n / k) -1; i++) q.push(k);
//	if (n%k)q.push(n%k);
//	
//	reverse(A, A + k);
//	while (q.size() != m-1) {
//		int cur = q.top(); q.pop();
//		q.push(1);
//		q.push(cur - 1);
//	}
//
//	int start = k;
//	while (!q.empty()) {
//		int cur = q.top(); q.pop();
//		reverse(A + start, A + start + cur);
//		start += cur;
//	}
//
//	for (int i = 0; i < n; i++)
//		printf("%d ", A[i]);
//	printf("\n");
//}
//
//
//
//
//
//

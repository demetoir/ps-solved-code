#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <string.h>

using namespace std;
typedef long long		LL;
typedef pair<int, int>	pii;

#define si(a)			scanf("%d",&(a))
#define sLL(a)			scanf("%lld",&(a))
#define all(a)			(a).begin(), (a).end()
#define INF				2e9

//codeforce 733c
vector<int> a, b,ansi;
vector< vector<int > > vset;
vector<char> ansc;
void no() {
	printf("NO");
	exit(0);
}

void f(int pre, vector<int> &v) {
	int idx = -1;
	int maxval = -1;
	for (int i = 0; i<v.size(); i++) {
		if (v[i] == maxval) {
			if (i - 1 >= 0 && v[i] > v[i-1]) 
				idx = i;
			if (i + 1 < v.size() && v[i] > v[i + 1]) 
				idx = i;
		}
		else if (v[i] > maxval) {
			maxval = v[i];
			idx = i;
		}
	}
	
	int sum = v[idx],i;
	int cur = idx;
	bool iscan = true;
	if (idx - 1 >= 0 && v[idx] > v[idx - 1]) {
		i = idx;
		while (i-1>=0) {
			if (sum > v[i-1]) {
				sum += v[i-1];
				ansi.push_back(cur+1 + pre);
				cur--;
				i--;
				ansc.push_back('L');
			}
			else {
				iscan = false;
				break;
			}
		}
		i = idx;
		while (i+1 < v.size()) {
			if (sum > v[i+1]) {
				sum += v[i+1];
				ansi.push_back(cur + 1 + pre);
				i++;
				ansc.push_back('R');
			}
			else {
				iscan = false;
				break;
			}
		}
	}
	else {
		i = idx;
		while (i + 1 < v.size()) {
			if (sum > v[i + 1]) {
				sum += v[i + 1];
				ansi.push_back(cur + 1 + pre);
				i++;
				ansc.push_back('R');
			}
			else {
				iscan = false;
				break;
			}
		}
		i = idx;
		while (i - 1 >= 0) {
			if (sum > v[i - 1]) {
				sum += v[i - 1];
				ansi.push_back(cur + 1 + pre);
				cur--;
				i--;
				ansc.push_back('L');
			}
			else {
				iscan = false;
				break;
			}
		}
	}

	if (iscan == false) no();
}


int n, k;
int main() {
	si(n);
	for (int i = 0,val; i < n; i++) {
		si(val);
		a.push_back(val);
	}
	si(k);
	for (int i = 0, val; i < k; i++) {
		si(val);
		b.push_back(val);
	}

	bool ispossible = true;
	int start = 0;
	int i ;
	for (i = 0; i < k; i++) {
		vector<int> temp;
		int sum = 0;
		bool iscan = false;
		for (int j = start; j < n; j++) {
			sum += a[j];
			temp.push_back(a[j]);
			if (sum == b[i]) {
				start = j + 1;
				iscan = true;
				f(i,temp);
			}
		}
		if (iscan == false) {
			ispossible = false;
			break;
		}
	}
	if (start != n) ispossible = false;

	if (ispossible) {
		printf("YES\n");
		for (int i = 0; i < ansi.size(); i++) {
			printf("%d %c\n", ansi[i], ansc[i]);
		}
	}
	else no();
	return 0;
}
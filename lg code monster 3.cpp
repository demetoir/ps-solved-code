////code moster 3
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <queue>
//#include <functional>
//using namespace std;
//
//#pragma warning(disable:4996)
//#define LL				long long 
//#define pii				pair<int, int>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define sLL(a)			scanf("%lld", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)			(a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAX_N			10001
//#define pb(a)			push_back((a))
//
//int n, w, k;
//bool find(int k, vector<pii> &v) {
//	if (k < 0) return false;
//
//	int l = INF, d = INF;
//	int r = -INF, u = -INF;
//	int li, di, ri, ui;
//	for (int i = 0; i < v.size(); i++) {
//		int x = v[i].first;
//		int y = v[i].second;
//
//		if (l > x) {
//			li = i;
//			l = x;
//		}
//
//		if (r < x) {
//			ri = i;
//			r = x;
//		}
//
//		if (d > y) {
//			di = i;
//			d = y;
//		}
//		if (u < y) {
//			ui = i;
//			u = y;
//		}
//	}
//
//	int thick = min((r - l) / 2, (u - d) / 2);
//	thick = min(w, thick);
//
//	int cnt = 0;
//	for (int i = 0; i < v.size(); i++) {
//		int x = v[i].first;
//		int y = v[i].second;
//		if ((x<l || x >r || y <d || y>u) ||
//			(x > l + thick && x< r - thick && y > d + thick && y < u - thick)) {
//			cnt++;
//		}
//	}
//	if (cnt <= k) return true;
//
//
//
//	bool f = false;
//	vector<pii> next;
//	next.clear();
//	for (int i = 0; i < v.size(); i++) {
//		if (i == li) continue;
//		next.push_back(v[i]);
//	}
//	f = max(find(k - 1, next),f);
//
//	next.clear();
//	for (int i = 0; i < v.size(); i++) {
//		if (i == ri) continue;
//		next.push_back(v[i]);
//	}
//	f = max(find(k - 1, next), f);
//
//	next.clear();
//	for (int i = 0; i < v.size(); i++) {
//		if (i == ui) continue;
//		next.push_back(v[i]);
//	}
//	f = max(find(k - 1, next), f);
//
//	next.clear();
//	for (int i = 0; i < v.size(); i++) {
//		if (i == di) continue;
//		next.push_back(v[i]);
//	}
//	f = max(find(k - 1, next), f);
//
//	return f;
//}
//vector<pii> v;
//int main() {
//	int test;
//	for (si(test); test > 0; test--) {
//		si(n); si(k); si(w);
//		v.clear();
//		for (int i = 0,a,b; i < n; i++) {
//			si(a); si(b);
//			v.push_back(pii(a, b));
//		}
//		int ans = find(k, v);
//		if (ans) printf("YES\n");
//		else printf("NO\n");
//	}
//	return 0;
//}
//
//
//
//
//
//////code moster 2
////#include <stdio.h>
////#include <algorithm>
////#include <vector>
////#include <queue>
////#include <functional>
////using namespace std;
////
////#pragma warning(disable:4996)
////#define LL				long long 
////#define pii				pair<int, int>
////#define si(a)           scanf("%d", &(a))
////#define sc(a)           scanf("%c", &(a))
////#define sLL(a)			scanf("%lld", &(a))
////#define ss(a)           scanf("%s", (a))
////#define all(a)			(a).begin() , (a).end()
////#define INF             2e9
////#define LLINF			1e17
////#define MAX_N			10001
////#define pb(a)			push_back((a))
////
////int ans;
////int n, k, w;
////vector<pii> cor;
////void init() {
////	ans = 0;
////	cor.clear();
////}
////void input() {
////	si(n); si(k); si(w);
////
////	for (int i = 0, a, b; i < n; i++) {
////		si(a); si(b);
////		cor.pb(pii(a, b));
////	}
////}
////
////bool cmp(pii a, pii b) {
////	return a.second < b.second;
////}
////int getpart(int x, vector<int> &v) {
////	int ret = lower_bound(all(v), x) - v.begin();
////	return ret;
////}
////int main() {
////	int test;
////	for (si(test); test > 0; test--) {
////		init();
////		input();
////
////		int left = INF, right = -INF;
////		for (int i = 0; i < n; i++) {
////			int x = cor[i].first, y = cor[i].second;
////			left = min(left, x);
////			right = max(right, x);
////		}
////		int thick = min((right - left) / 2, w);
////		sort(all(cor), cmp);
////		vector<int> lv, rv, mv, ycor;
////
////		for (int i = 0; i < n; i++) {
////			int x = cor[i].first, y = cor[i].second;
////
////			if (left <= x && x <= left + thick)	lv.pb(cor[i].second);
////			else if (right - thick <= x && x <= right) rv.pb(cor[i].second);
////			else mv.pb(cor[i].second);
////			ycor.push_back(cor[i].second);
////		}
////
////		sort(all(mv));
////		sort(all(lv));
////		sort(all(rv));
////		sort(all(ycor));
////
////		//전처리
////		vector<int> ridx, midx, lidx;
////		lidx = vector<int>(lv.size());
////		for (int i = 0, endidx; i<lv.size(); i++) {
////			while (lv[i] - lv[endidx] > w) endidx++;
////			lidx[i] = endidx;
////		}
////
////		midx = vector<int>(mv.size());
////		for (int i = 0, endidx; i<mv.size(); i++) {
////			while (mv[i] - mv[endidx] > w) endidx++;
////			midx[i] = endidx;
////		}
////
////		ridx = vector<int>(rv.size());
////		for (int i = 0, endidx; i<rv.size(); i++) {
////			while (rv[i] - rv[endidx] > w) endidx++;
////			ridx[i] = endidx;
////		}
////
////		vector<int> memo1, memo2;
////		int downval = 0;
////
////		for (int i = 1, endidx = 0; i < n; i++) {
////			int yline = ycor[i];
////			// up 이번것 갱신
////
////
////
////			// down 전에거 최대값 갱신
////		}
////
////
////
////		if (ans)printf("YES\n");
////		else printf("NO\n");
////	}
////	return 0;
////}
////
////

////정답코드...
//#include <iostream>
//#include <cstdio>
//#include <cstring>
//#include <vector>
//#include <queue>
//#include <algorithm>
//#include <math.h>
//#include <string.h>
//#include <functional>
//
//#define ll              long long int
//#define pll             pair<long long,pair<int, int> >
//#define pii             pair<long long, long long>
//#define FOR(a,b,c)      for((a)=(b);(a)<=(c);(a)++)
//#define _FOR(a,b,c)     for((a)=(b);(a)<(c);(a)++)
//#define INF             2e9
//#define mod             1000000007
//#define MAX_E             50001
//#define MAX_V           50001
//
//using namespace std;
//
//
//ll N, K, W;
//pii cood[MAX_V];
//ll inwall[MAX_V], outwall[MAX_V];
//
//bool cmp_y(const pii& a, const pii& b)
//{
//	return a.second < b.second;
//}
//
//bool cmp_x(const pii& a, const pii& b)
//{
//	return a.first > b.first;
//}
//
//int main() {
//	ll t;
//	scanf("%lld", &t);
//	while (t--)
//	{
//		scanf("%lld %lld %lld", &N, &K, &W);
//		ll min_x = 2000000000, max_x = -2000000000;
//
//		for (int i = 0; i < N; i++)
//		{
//			ll x, y;
//			scanf("%lld %lld", &x, &y);
//			cood[i] = pii(x, y);
//			min_x = min(x, min_x);
//			max_x = max(x, max_x);
//		}
//
//		ll in_wall_size = 0, out_wall_size = 0;
//
//		for (int i = 0; i < N; i++)
//		{
//			if (cood[i].first <= min_x + W || cood[i].first >= max_x - W)
//			{
//				inwall[in_wall_size++] = cood[i].second;
//			}
//			else {
//				outwall[out_wall_size++] = cood[i].second;
//			}
//		}
//
//		sort(inwall, inwall + in_wall_size);
//		sort(outwall, outwall + out_wall_size);
//		sort(cood, cood + N, cmp_y);
//
//		//lower
//
//		//printf("in : %lld out : %lld\n",in_wall_size,out_wall_size);
//
//		ll max_lower = -2000000000;
//
//		for (int i = 0; i < N; i++)
//		{
//			ll y = cood[i].second;
//			ll a = upper_bound(outwall, outwall + out_wall_size, y + W) - outwall;
//			ll ix = lower_bound(outwall, outwall + out_wall_size, y) - outwall;
//
//			a -= ix;// - (outwall[a] == y?1:0);
//
//			ll b = lower_bound(inwall, inwall + in_wall_size, y) - inwall;
//			//b -= (inwall[b] == y?1:0);
//
//			//printf("%lld : %lld %lld\n",cood[i].second,a,b);
//			max_lower = max(max_lower, a - b);
//		}
//
//		// printf("---------------------------------------\n");
//
//		ll max_upper = -2000000000;
//
//		for (int i = 0; i < N; i++)
//		{
//			ll y = cood[i].second;
//			ll a = upper_bound(outwall, outwall + out_wall_size, y + W) - outwall;
//			ll ix = lower_bound(outwall, outwall + out_wall_size, y) - outwall;
//
//			a -= ix;// - (outwall[a] == y?1:0);
//
//			ll b = in_wall_size - (upper_bound(in wall, in wall + in_wall_size, y + W) - in wall);
//			//b -= (inwall[b] == y?1:0);
//
//
//			//printf("%lld : %lld %lld\n",cood[i].second,a,b);
//			max_upper = max(max_upper, a - b);
//		}
//
//		//printf("upper : %lld lower : %lld\n",max_upper,max_lower);
//
//		if ((out_wall_size - max_lower - max_upper) <= K)
//			printf("YES\n");
//		else printf("NO\n");
//
//
//	}

//
////정답 코드
//
//
//
//#include <stdio.h>
//#include <algorithm>
//#include <vector>
//#include <queue>
//#include <functional>
//using namespace std;
//
//
//#pragma warning(disable:4996)
//#define LL				long long 
//#define pii				pair<int, int>
//#define si(a)           scanf("%d", &(a))
//#define sc(a)           scanf("%c", &(a))
//#define sLL(a)			scanf("%lld", &(a))
//#define ss(a)           scanf("%s", (a))
//#define all(a)			(a).begin() , (a).end()
//#define INF             2e9
//#define LLINF			1e17
//#define MAXN				10001
//#define pb(a)			push_back((a))
//
//struct Segtree {
//	struct NODE {
//		int first, last;
//		int minval;
//		NODE *left, *right;
//		NODE(int first, int last) : first(first), last(last), minval(INF) {
//			if (first != last) {
//				int mid = (first + last) / 2;
//				left = new NODE(first, mid);
//				right = new NODE(mid + 1, last);
//			}
//		}
//
//		void update(int pos, int value) {
//			if (first == last)	minval = value;
//			else {
//				if (pos <= (first + last) / 2) left->update(pos, value);
//				else right->update(pos, value);
//				minval = min(left->minval, right->minval);
//			}
//		}
//
//		int query(int lo, int hi) {
//			if (hi < first || last < lo) return INF;
//			if (lo <= first && last <= hi) return minval;
//			return min(left->query(lo, hi), right->query(lo, hi));
//		}
//	};
//
//	NODE* root;
//	Segtree(int n) : root(new NODE(0, n - 1)) { }
//
//	void update(int pos, int value) { root->update(pos, value); }
//	int query(int lo, int hi) { return root->query(lo, hi); }
//};
//
//int n, m, q;
//int parent[MAXN];
//vector<int> children[MAXN];
//int subtree_size[MAXN];
//int depth[MAXN];
//
//vector<vector<int> > heavy_paths;
//vector<int> heavy_path_index;
//
//vector<int> exp_ancestor[MAXN];
//vector<Segtree> segforest;
//void lca_dfs(int cur) {
//	subtree_size[cur] = 1;
//
//	exp_ancestor[cur] = vector<int>(1, parent[cur]);
//	for (int log_jump = 0; ; ++log_jump) {
//		int arrived = exp_ancestor[cur][log_jump];
//		if (exp_ancestor[arrived].size() <= log_jump) break;
//		int next = exp_ancestor[arrived][log_jump];
//		exp_ancestor[cur].push_back(next);
//	}
//
//	for (int child : children[cur]) {
//		depth[child] = depth[cur] + 1;
//		lca_dfs(child);
//		subtree_size[cur] += subtree_size[child];
//	}
//}
//
//void heavy_light_decomposition(int root) {
//	heavy_paths.clear();
//	heavy_path_index.resize(n + 1, -1);
//
//	queue<int> q;
//	q.push(root);
//	while (!q.empty()) {
//		int cur = q.front(); q.pop();
//
//		for (int child : children[cur])
//			q.push(child);
//
//		if (cur == root) continue;
//
//		int p = parent[cur];
//
//		if (subtree_size[cur] * 2 >= subtree_size[p] && p != root) {
//			int parent_path_index = heavy_path_index[p];
//			heavy_paths[parent_path_index].push_back(cur);
//			heavy_path_index[cur] = parent_path_index;
//		}
//		else {
//			heavy_path_index[cur] = heavy_paths.size();
//			heavy_paths.push_back(vector<int>(2));
//			heavy_paths.back()[0] = p;
//			heavy_paths.back()[1] = cur;
//		}
//	}
//}
//
//void initialize_trees() {
//	segforest.clear();
//	segforest.reserve(heavy_paths.size());
//	for (const auto& path : heavy_paths) {
//		int m = path.size();
//		segforest.push_back(Segtree(m - 1));
//		for (int i = 0; i < m - 1; ++i)
//			segforest.back().update(i, 1);
//	}
//}
//
//int lca(int u, int v) {
//	if (depth[u] > depth[v]) swap(u, v);
//
//	int diff = depth[v] - depth[u];
//	for (int i = 0; (1 << i) <= diff; ++i)
//		if (diff & (1 << i))
//			v = exp_ancestor[v][i];
//
//	if (u == v) return u;
//
//	for (int i = exp_ancestor[u].size() - 1; i >= 0; --i)
//		if (i < exp_ancestor[u].size() && exp_ancestor[u][i] != exp_ancestor[v][i]) {
//			u = exp_ancestor[u][i];
//			v = exp_ancestor[v][i];
//		}
//
//	return exp_ancestor[u][0];
//}
//
//int find_edge_in_path(int path_index, int v) {
//	int top_of_path = heavy_paths[path_index][0];
//	return depth[parent[v]] - depth[top_of_path];
//}
//
//void update(int u, int v, int cost) {
//	if (parent[u] == v) swap(u, v);
//
//	int path_index = heavy_path_index[v];
//	int index_in_path = find_edge_in_path(path_index, v);
//	segforest[path_index].update(index_in_path, cost);
//}
//
//int query_topdown(int u, int v) {
//	if (u == v) return INF;
//
//	if (heavy_path_index[u] == heavy_path_index[v]) {
//		int path_index = heavy_path_index[u];
//		int first_edge = find_edge_in_path(path_index, u) + 1;
//		int last_edge = find_edge_in_path(path_index, v);
//		return segforest[path_index].query(first_edge, last_edge);
//	}
//
//	int path_index = heavy_path_index[v];
//	int top_of_path = heavy_paths[path_index][0];
//
//	int last_edge = find_edge_in_path(path_index, v);
//	return min(query_topdown(u, top_of_path),
//		segforest[path_index].query(0, last_edge));
//}
//
//int query(int u, int v) {
//	int t = lca(u, v);
//
//	int a = query_topdown(t, u);
//	int b = query_topdown(t, v);
//	return min(a, b);
//}
//
//LL ans;
//int uftree[10001];
//int ranktree[10001];
//int find(int x) {
//	if (x == uftree[x]) return x;
//	return uftree[x] = find(uftree[x]);
//}
//void unite(int a, int b) {
//	int A = find(a), B = find(b);
//	if (A == B)return;
//	if (ranktree[A] <= ranktree[B]) {
//		uftree[B] = A;
//		if (ranktree[A] == ranktree[B]) ranktree[B]++;
//	}
//	else {
//		uftree[A] = B;
//	}
//}
//struct EDGE {
//	int a, b, c;
//	EDGE(int a, int b, int c) :a(a), b(b), c(c) {}
//};
//bool cmp(EDGE a, EDGE b) {
//	return a.c > b.c;
//}
//
//vector<EDGE> edgelist;
//vector <pii> spantree[10001];
//
//int check[12345];
//void make_tree_dfs(int cur, int p) {
//	if (check[cur]) return;
//	check[cur] = true;
//	parent[cur] = p;
//	for (int i = 0; i < spantree[cur].size(); i++) {
//		int next = spantree[cur][i].first;
//		make_tree_dfs(next, cur);
//	}
//}
//
//vector<EDGE> make_spaning_tree() {
//	int cnt = 0;
//	sort(all(edgelist), cmp);
//	vector<EDGE> list;
//	for (int i = 0; i < edgelist.size(); i++) {
//		if (cnt == n - 1) break;
//		int a = edgelist[i].a;
//		int b = edgelist[i].b;
//		int c = edgelist[i].c;
//
//		if (find(a) == find(b)) continue;
//
//		unite(a, b);
//		list.push_back(edgelist[i]);
//		spantree[a].pb(pii(b, c));
//		spantree[b].pb(pii(a, c));
//		cnt++;
//	}
//
//	int root = 0;
//	memset(parent, 0, sizeof(parent));
//
//	memset(check, 0, sizeof(check));
//	make_tree_dfs(root, -1);
//
//	return list;
//}
//
//int main() {
//	int test;
//	for (si(test); test > 0; test--) {
//		edgelist.clear();
//		ans = 0;
//		for (int i = 0; i <= 10000; i++) {
//			spantree[i].clear();
//			uftree[i] = i;
//			ranktree[i] = 0;
//		}
//		si(n); si(m);
//		for (int i = 0, a, b, c; i < m; i++) {
//			si(a); si(b); si(c);
//			a--; b--;
//			edgelist.push_back(EDGE(a, b, c));
//		}
//		vector<EDGE> list = make_spaning_tree();
//		for (int i = 0; i < MAXN; ++i) children[i].clear();
//		for (int i = 0; i <n; ++i) {
//			if (parent[i] != -1)
//				children[parent[i]].push_back(i);
//		}
//
//		lca_dfs(0);
//		heavy_light_decomposition(0);
//		initialize_trees();
//
//		//update
//		for (int i = 0; i < list.size(); i++) {
//			int a = list[i].a;
//			int b = list[i].b;
//			int c = list[i].c;
//			update(a, b, c);
//		}
//
//		si(q);
//		for (int a, b; q > 0; q--) {
//			si(a); si(b);
//			a--;
//			b--;
//			if (a == b) continue;
//			ans += query(a, b);
//		}
//
//		printf("%lld\n", ans);
//	}
//	return 0;
//}

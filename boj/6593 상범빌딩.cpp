//6593 상범빌딩
//bfs 순회
//디스크립션 오타 ㅅㅂ
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define LL				long long 
#define si(a)			scanf("%d",&(a))
#define sc(a)			scanf("%c",&(a))
#define ss(a)			scanf("%s",(a))

#define all(x)			(q).begin(),(q).end()
#define pii				pair<int, int>
#define INF				2e9

#define MAXN			101
#define BITSIZE			21
int l, r, c;
char map[123][123][123];

int dist[123][123][123];

int sx, sy, sz, ex,ey,ez;
struct D {
	int x,y,z;
	D() {};
	D(int x, int y, int z) :x(x), y(y), z(z) {};
}d;
int dx[6] = { 1,-1,0,0,0,0};
int dy[6] = { 0,0,1,-1,0,0};
int dz[6] = { 0,0,0,0,1,-1};

int main() {
	while (1) {
		si(l);	si(r);	si(c);
		if (l == 0 && r == 0 && c == 0) break;

		for (int i = 0; i < l; i++) {
			for (int j = 0; j < r; j++) {
				char str[123];
				ss(str);
				for (int k = 0; k < c; k++) {
					dist[i][j][k] = INF;
					map[i][j][k] = str[k];
					if (str[k] == 'S') {
						sx = k;
						sy = j;
						sz = i;
					}
					if (str[k] == 'E') {
						ex = k;
						ey = j;
						ez = i;
					}
				}
			}
		}

		queue<D>q;
		q.push(D(sx, sy, sz));
		dist[sz][sy][sx] = 0;
		int ans = -1;
		while (!q.empty()) {
			int x = q.front().x;
			int y = q.front().y;
			int z = q.front().z;
			q.pop();

			for (int i = 0; i < 6; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				int nz = z + dz[i];

				if (nx < 0 || nx >= c || ny < 0 || ny >= r || nz < 0 || nz >= l || map[nz][ny][nx] == '#')continue;

				if (dist[nz][ny][nx] > dist[z][y][x] + 1) {
					dist[nz][ny][nx] = dist[z][y][x] + 1;
					q.push(D(nx, ny, nz));
				}
			}
		}

		if (dist[ez][ey][ex] == INF) printf("Trapped!\n");
		else printf("Escaped in %d minute(s).\n",dist[ez][ey][ex]);
	}
	return 0;
}








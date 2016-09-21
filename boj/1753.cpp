#include <stdio.h>
#include <queue>
#include <vector>
using namespace std;
const long INF= 987654321;
typedef pair<long,long> pi;

int main(){
	queue <long> q;	
	vector<pi> G[20001];
	
	long long V,E,start;
	scanf("%lld %lld %lld",&V,&E,&start);
	
	for (int i=0; i<E;i++){
		int u,v,w;
		scanf("%d %d %d",&u,&v,&w);
		G[u].push_back(pi(v,w));

	}
	vector<long> distance(V+1,INF);
	distance[start]=0;
	q.push(start);
	
	while(!q.empty()){
		long cur=q.front();
		q.pop();
		for(int i=0;i<G[cur].size();i++){
			long n=G[cur][i].first;
			long w=G[cur][i].second;
			if( distance[n]>distance[cur]+w){
				distance[n]=distance[cur]+w;
				q.push(n);
			}
		}
		
	}
	for(int i=1;i<V+1;i++){
		if( distance[i]==INF)
			printf("INF\n");
		else 
			printf("%ld\n",distance[i]);
	}
	return 0;
}
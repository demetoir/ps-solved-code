
## C CODE



#include <stdio.h>


using namespace std;
int n=200;
int memo[201][201][201];
int val=0;
int a,b,c,d,e,f,t;

void make(){
    for(int i=1;i<200+1;i++){        
        for(int j=1; j<i+1;j++){
            for(int k=1;k<j+1;k++){
                
                //printf("###%d %d %d\n",i,j,k);
                if (i==j and j==k)
                    val=0;
                else
                    val = 987654;                
    
                for(int s=1;s<i/2+1;s++){
                    a=s;b=j;c=k;
                    d=i-s;e=j;f=k;

    
                    if (b < c){t=b;b=c;c=t;}
                    if (a < b){t=a;a=b;b=t;}
                    if (b < c){t=b;b=c;c=t;}

    
                    if (e < f){t=e;e=f;f=t;}
                    if (d < e){t=d;d=e;e=t;}
                    if (e < f){t=e;e=f;f=t;}
                    /*
                    printf("%d %d %d %d\n",a,b,c,memo[a][b][c]);
                    printf("%d %d %d %d\n",d,e,f,memo[d][e][f]);
                    printf("\n");
                    */
                    if (val > memo[d][e][f] + memo[a][b][c]+1)
                        val=memo[d][e][f] + memo[a][b][c]+1;
                
                }
    
                for(int s=1;s<j/2+1;s++){ 
                    a=i;b=s;c=k;
                    d=i;e=j-s;f=k;

    
                    if (b < c){t=b;b=c;c=t;}
                    if (a < b){t=a;a=b;b=t;}
                    if (b < c){t=b;b=c;c=t;}

    
                    if (e < f){t=e;e=f;f=t;}
                    if (d < e){t=d;d=e;e=t;}
                    if (e < f){t=e;e=f;f=t;}
                    /*
                    printf("%d %d %d %d\n",a,b,c,memo[a][b][c]);
                    printf("%d %d %d %d\n",d,e,f,memo[d][e][f]);
                    printf("\n");
                    */
                    if (val > memo[d][e][f] + memo[a][b][c]+1)
                        val=memo[d][e][f] + memo[a][b][c]+1;
                }
                for(int s=1;s<k/2+1;s++){
                    a=i;b=j;c=s;
                    
                    d=i;e=j;f=k-s;
    
                    if (b < c){t=b;b=c;c=t;}
                    if (a < b){t=a;a=b;b=t;}
                    if (b < c){t=b;b=c;c=t;}

    
                    if (e < f){t=e;e=f;f=t;}
                    if (d < e){t=d;d=e;e=t;}
                    if (e < f){t=e;e=f;f=t;}
                    /*
                    printf("%d %d %d %d\n",a,b,c,memo[a][b][c]);
                    printf("%d %d %d %d\n",d,e,f,memo[d][e][f]);
                    printf("\n");
                    */    
                    if (val > memo[d][e][f] + memo[a][b][c]+1)
                        val=memo[d][e][f] + memo[a][b][c]+1;
    
                }
                memo[i][j][k] = val;
                //printf("###%d %d %d %d\n",i,j,k,val);
                //printf("\n");
            }
        }
    }
    
    
}

int main(){

    
    scanf("%d",&n);
    make();
    

    
    for(int i=0;i<n;i++){
        scanf("%d %d %d",&a,&b,&c);
        if (b < c){t=b;b=c;c=t;}
        if (a < b){t=a;a=b;b=t;}
        if (b < c){t=b;b=c;c=t;}
        printf("%d\n", memo[a][b][c]+1);
    }
    
    return 0;
    

}
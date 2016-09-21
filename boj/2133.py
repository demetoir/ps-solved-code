b={0:1}
def f(k):
 s=0
 if k in b:return b[k]
 for i in range(2,k+1,2):s+=f(k-i)*2
 b[k]=s+f(k-2);return b[k]
k=int(input())
print(f(k)if k%2==0 else 0)
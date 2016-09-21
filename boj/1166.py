from decimal import *
n,l,w,h=map(int,raw_input().split())
getcontext().prec=30
l,w,h=Decimal(l),Decimal(w),Decimal(h)
lo=Decimal(0.0)
hi=Decimal(98765432100.0)
ans=Decimal(0.0)
for i in range(10000):
	mid=Decimal((lo+hi)/2)
	a=(l//mid)*(w//mid)*(h//mid)
	if n<=(l//mid)*(w//mid)*(h//mid):
		lo=mid
	else:
		hi=mid

print mid

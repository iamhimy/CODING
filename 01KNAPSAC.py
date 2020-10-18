from itertools import combinations
w=list(map(int,input().split()))
v=list(map(int,input().split()))
g={t[0]:t[1] for t in zip(w,v)}
W=int(input())
c=[]
for i in range(1,len(w)+1):
    cmb=combinations(w,i)
    cm=list(cmb)
    c.extend(cm)
m=0
for i in c:
  if (sum(i)<=W):
      s=0
      for j in i:
          s+=g[j]
      if s>m:
          m=s
print(m) 

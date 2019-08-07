m=int(input())
n=list(map(int,input().split()))
c=0
for i in range(0,len(n)):
    c=c+n[i]
b=c//m
print(b)

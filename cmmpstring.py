n=list(input().split())
if len(n[0])==len(n[1]):
    print(n[1])
elif len(n[0])>len(n[1]):
    print(n[0])
else:
    print(n[1])

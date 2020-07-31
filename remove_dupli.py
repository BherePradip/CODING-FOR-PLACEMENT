a=list(map(int,input().split()))
r=[]
for i in a:
    if i not in r:
        r.append(i)
print(r)

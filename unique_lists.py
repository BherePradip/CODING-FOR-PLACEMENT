l=list(map(int,input().split()))
m=list(map(int,input().split()))
flag=1
for i in l:
    if i in m:
        flag=0
        break
if(flag==0):
    print("not unique" )
else:
    print("unique")

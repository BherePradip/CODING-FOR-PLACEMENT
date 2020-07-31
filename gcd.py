a=int(input())
b=int(input())
if(a<b):
    small=a
else:
    small=b
for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        ans=i
print(ans)

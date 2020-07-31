a=int(input())
b=int(input())
if(a==0 or b==0):
    print(0)
else:
    n=(a*b)+1
    if(a>b):
        m=a
    else:
        m=b
    for i in range(m,n,+1):
        if(i%a==0 and i%b==0):
            print(i)
            break

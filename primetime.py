a,b=map(int,input().split())
m=[]
for i in range(a//b):
    n=[]
    for i in range(b):
        n.append(0)
    m.append(n)
c=b
r=a//b
count=0
ans=0
for j in range(c):
    for i in range(r):
        m[i][j]=count+1
        count+=1
for i in m:
    flag=0
    for j in i:
        if(j==1):
            flag+=1
        elif(j==2):
            flag+=0
        else:
            for k in range(2,j):
                if(j%k==0):
                    flag+=1
                    break
    if(flag==0):
        ans+=1
        print(i)        
print(ans)    

        

    
    

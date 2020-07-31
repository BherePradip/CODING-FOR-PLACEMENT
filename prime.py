lower=int(input())
upper=int(input())
done=0
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                
                break
        else:
            done+=1
            print(num)
        if(done==5):
            break

    
        
    
    

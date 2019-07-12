# sorted-prime
i=int(input())
c=0
for s in range(2,i+1):
    if i%s==0:
        C=0
        for j in range(2,s+1):
            if s%j==0 and s!=j:
                c=1
                break
        if c==0:
            print(j,end=' ')
            

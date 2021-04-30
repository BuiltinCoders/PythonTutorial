def sieveOfErosthen(m):
    limit=m+1
    prime=[True]*limit

    for i in range(2,int(m**0.5)):
        if prime[i]:
            for x in range(i*i,limit,i):
                prime[x]=False
    return prime  

def segmentedSieve(m,n):
    limit= n+1
    segment=[True]*limit

    for j in range(2,int(n**0.5) ):
        if sieveOfErosthen(j):
            for b in range(j*(m//j),limit,j):
                if b >j:
                    segment[b]=False
    for v in range(m,limit):
        if segment[v]:
            print(v)
    return True
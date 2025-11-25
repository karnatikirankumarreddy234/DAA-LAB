def power(x,n):
    if(n==0):
        return 1
    temp= power(x,n//2)
    if(n%2==0):
        return temp * temp
    else:
        return temp * temp *x

x=5
n=3
print(power(5,3))    

    
    
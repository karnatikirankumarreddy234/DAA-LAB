def karatsuba(x,y):
    if (x<10 or y<10):
        return x*y
    M=max (len(str(x)),len(str(y)))
    if M%2!=0:
        M-=1
    a,b=divmod(x,10**int(M/2))
    c,d=divmod(y,10**int(M/2))
    
    ac=karatsuba(a,b)
    bd=karatsuba(b,d)
    abcd=karatsuba((a+b),(c+b))-ac-bd

    return(ac*(10**M)+(bd)+(abcd*(10*int(M/2))))

x=153
y=1223
print(karatsuba(x,y))   


    
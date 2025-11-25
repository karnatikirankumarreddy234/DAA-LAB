
def power(base,exponent):
    result=1
    for i in range(exponent):
        result=result*base
    return result
    
base=2
exponent=5
res=power(base,abs(exponent))
if(exponent<0):
   res=1/res
print(res)

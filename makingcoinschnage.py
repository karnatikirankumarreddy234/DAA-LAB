def makingcoinchange(coins,amount):
    mcm=[float('inf')]*(amount+1)
    mcm[0]=0
    for coin in coins:
        for i in range (coin,amount+1):
            mcm[i]=min(mcm[i],1+mcm[i-coin])
    return mcm[amount]


coins=[0,5,6,8,18,10,51,26]
amount=11
print(makingcoinchange(coins,amount))



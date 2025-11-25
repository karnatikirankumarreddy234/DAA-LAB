values=[100,200,350]
weight=[10,25,50]
cap=50
ratio=[v/w for v,w in zip(values,weight)]
zipp=zip(ratio,values,weight)
zipp=sorted(zipp,reverse=True)
profit=0

for i in zipp:
    if i[2]<=cap:
        profit=profit+i[1]
        cap=cap-i[2]
print(profit)

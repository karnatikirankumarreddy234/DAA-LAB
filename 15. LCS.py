def lcs(x,y):
    m=len(x)
    n=len(y)
    l=[[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (x[i-1]==y[j-1]):
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][n]

x="longest"
y="stone"
print(lcs(x,y))
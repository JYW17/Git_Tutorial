case = int(input())

for i in range(case):
    k = int(input())
    n = int(input())
    
    
    lis = [([0 for j in range(n)]) for p in range(k+1)]
    
    for j in range(n):
        lis[0][j] = j+1
    for j in range(1,k+1):
        lis[j][0] = 1
        for p in range(1,n):
            lis[j][p] = lis[j][p-1] + lis[j-1][p]
    print(lis[k][n-1])
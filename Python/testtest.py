num = int(input())
lis = list()

for i in range(num):
    lis.append(input())

for i in lis:
    count = 0
    score = 0
    for j in i:
        if j == "O":
            score += 1
            count += score
        else:
            score = 0
    print(count)
    

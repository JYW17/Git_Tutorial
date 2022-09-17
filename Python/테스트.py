import sys
sys.setrecursionlimit(10**6)

list = [0 for i in range(1001)]
list[1] = 1
list[2] = 2

def tile(num):
    if list[num] != 0:
        return list[num]
    list[num] = (tile(num-1) + tile(num-2))%10007
    return list[num]

num = int(input())
print(tile(num))
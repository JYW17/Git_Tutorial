num = int(input())
list = [0 for i in range(100)]
list[0] = 0
list[1] = 1
for i in range(2, 100):
    list[i] = list[i-1] + list[i-2]

print(list[num])
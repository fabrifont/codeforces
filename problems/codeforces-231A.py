n = int(input())
l = [0, 0, 0]
count = 0
for i in range(1, n + 1):
    l = input().split()
    l = list(map(int, l))
    if (l[0] and l[1]) or (l[0] and l[2]) or (l[1] and l[2]):
        count += 1
print(count)

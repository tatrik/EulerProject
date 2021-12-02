d = {}
n = 0
for i in range(0, 100000):
    n = n + i + 1
    d[n] = []
    for j in range(0, i+2):
        if j != 0:
            if n % j == 0:
                d[n].append(j)
print(d)


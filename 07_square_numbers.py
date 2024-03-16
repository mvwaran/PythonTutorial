# 1 4 9 16 25 36 .....

output = []
n = 20

for i in range(1, n + 1):
    # 2 x 2
    # 3 x 3
    # 4 x 4
    # i x i
    output.append(i * i)

print(output)
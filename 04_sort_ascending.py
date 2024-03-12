num = [7, 2, 9, 1, 5]

# i, j
# 0, 1
# 0, 2
# 0, 3
# 0, 4
# 1, 2
# 1, 3
# 1, 4
# 2, 3
# 2, 4
# 3, 4

for i in range(0, len(num) - 1):
    for j in range(i + 1, len(num)):
        if num[i] >= num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print(num)
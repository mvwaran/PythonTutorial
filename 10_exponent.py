n = 40
output = []

# 1 - 1 - pow(2, 0)
# 2 - 2 - pow(2, 1)
# 3 - 4 - pow(2, 2)
# 4 - 8 - pow(2, 3)
# 5 - 16 - pow(2, 4)
# 6 - 32 - pow(2, 5)
# 7 - 64 - pow(2, 6)

for i in range(1, n + 1):
    # pow(2, i - 1)
    out = pow(2, i - 1)
    output.append(out)

print(output)
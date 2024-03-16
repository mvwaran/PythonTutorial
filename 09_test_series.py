# BODMAS

n = 10
output = []

for i in range(1, n + 1):
    # (i^2 + 1) / i
    out = (pow(i, 2) + 1) / i
    output.append(out)

print(output)
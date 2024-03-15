# 1 2 3 5 8 13 21 ............
# Print fibonacci series upto 10 numbers

output = [1, 2]

# for i in range(1, 9):
#     a = output[len(output) - 1]
#     b = output[len(output) - 2]
#     output.append(a + b)

for i in range(1, 9):
    a = output[-1]
    b = output[-2]
    output.append(a + b)

print(output)
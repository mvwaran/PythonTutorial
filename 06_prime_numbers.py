# 1 2 3 5 7 11 13 
# Print 20 prime numbers

n = 5

output = []
counter = 0
i = 1

while counter < n:
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if isPrime == True:
        counter = counter + 1
        output.append(i)
    i = i + 1

print(output)
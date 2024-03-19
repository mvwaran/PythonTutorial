def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def echo(a):
    print(a)

def greetMorning():
    print("Good Morning")

def prime(n):
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
    return output

a = prime(30)
b = prime(10)
print(a)
print(b)
n = int(input("Enter N: "))

factorial = 1
total = 0

for i in range(1, n + 1):
    factorial = factorial * i
    total = total + factorial

print("Sum of factorials:", total)

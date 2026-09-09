x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

total = 0

for i in range(n):
    power = 2 * i + 1

    # Calculate factorial
    factorial = 1
    for j in range(1, power + 1):
        factorial = factorial * j

    term = (x ** power) / factorial

    if i % 2 == 0:
        total = total + term
    else:
        total = total - term

print("Sum of series:", total)

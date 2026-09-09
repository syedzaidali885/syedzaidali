num = int(input("Enter a number: "))

original = num
digits = 0
temp = num

# Count the number of digits
while temp > 0:
    digits = digits + 1
    temp = temp // 10

# Calculate the sum of digits raised to the number of digits
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

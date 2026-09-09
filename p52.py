num = int(input("Enter a number: "))

seen = set()

while num != 1 and num not in seen:
    seen.add(num)
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit * digit
        num = num // 10

        num = sum

if num == 1:
    print("Happy number")
else:
    print("Not a happy number")            
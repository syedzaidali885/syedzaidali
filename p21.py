age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age <= 59:
    price = 100
else:
    price = 50
print("Ticket price =", price)               
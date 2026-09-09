a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print("Largest is", a)
elif b > c and b > a:
    print("Largest is", b)
else:
    print("Largest is", c)         

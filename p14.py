n = int(input("Enter a number: "))
k = int(input("Enter the bit position(k): "))

if n & (1 << k):
    print("kth bit is SET")
else:
    print("kth bit is NOT SET")    
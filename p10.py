char = input("Enter a single character: ")

if len(char) == 1:
    if char.isupper():
        print("Uppercase character")
    elif char.islower():
        print("Lowercase character")
    elif char.isdigit():
        print("Digit")
    else:
        print("Special character")            
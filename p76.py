def count_vowels(s, index):
    if index == len(s):
        return 0

    if s[index].lower() in "aeiou":
        return 1 + count_vowels(s, index + 1)
    else:
        return count_vowels(s, index + 1)


text = input("Enter a string: ")

result = count_vowels(text, 0)

print("Number of vowels:", result)

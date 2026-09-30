string = input("Enter a string: ")

frequency = {}

for letter in string:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print("Letter frequency:")

for letter in frequency:
    print(letter, ":", frequency[letter])
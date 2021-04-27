# write a program that finds the char that appears most frequesntly in a string

letters = dict()

str = "I cannot seeeeeem to figure out this probleeeeeeem"

for char in str:
    if char in letters:
        letters[char] = letters[char] + 1
    else:
        letters[char] = 1

print(letters)

maxCount = 0

for char in letters:
    if letters[char] > maxCount:
        maxCount = letters[char]
        maxChar = char

print(maxChar)

import math

n = int(input("Please enter a number : "))

fact = math.factorial(n)

print(fact)

m = int(input("Please enter a number : "))

i = 1 

my_array = []

while i <= 10:
    result = m * i
    my_array.append(result)
    i += 1

print(my_array)

l = int(input("Please enter a number : "))

sqr = math.sqrt(l)

if  type(sqr) == int:
    print(True) 
else:
    print(False)

string = str(input("Please enter a string : "))
words = string.split(" ")
print(words)
lenghts = {}
for word in words:
    lenghts[word] = len(word)
print(max(lenghts.values()))

ch = str(input("Please enter a string : "))

letters = {}

for word in ch:
    for letter in word:
        if letter not in letters :
            letters[letter] = 1
        elif letter in letters:
            letters[letter] += 1

print(letters) 


# Here is a loop that advances an index through a sequence of characters
# until finding an entry with value 'X' or reaching the end of the sequence.

j = 0
while j <len(data) and data[j] != 'X':
    j += 1

# for loop structure
# can be used on any iterable structure such as list, tuple, str, set, dict, or file
for element in iterable:
    body

# to find the maximum value in a list of elements
biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val

# Rather than looping over the elements in the list, we can loop through all possible
# indices of the list range generates the series of n values from 0 to n - 1.

# Standard Python idiom for looping through the series of indices of a data sequence
for j in range(len(data)):

# To find the index of the maximum element of a list:
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j

# Break statement immediately terminates a while or for loop when executed within its body
# If applied within nested control structures, it causes the termination of
# the most immediately enclosing loop.

# Here is code that determines whether a target value occurs in a data set
found = False
for item in data:
    if item == target:
        found = True
        break

# continue causes the current iteration of a loop body to stop, but with subsequent
# passes of the loop proceeding as expected


# You can use simultaenous assingment to swap
j, k = k, j

# alternative swap
temp = j
j = k
k = temp

# fibonacci using simultaneous assignments
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# find the max in a list
def max(data):
    max = data[0]
    for num in data:
        if num > data[0]:
            max = num
    print(max)

max([1,2])

# Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
my_list = [2**n for n in range(9)]
print(my_list)


# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).
def is_distinct(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return False
        else:
            seen[num] = True
    else:
        return True

my_sequence = [1, 2, 3, 4, 5]
result = is_distinct(my_sequence)
print(result)

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

result_list = [i * (i + 1) for i in range(10)]

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list[ a , b , c ,..., z ],but without having to type all 26 such characters literally.

import string

alphabet_list = [char for char in string.ascii_lowercase]
print(alphabet_list)

# Write a short Python function that counts the number of vowels in a given
# character string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


# slice [start:stop:step]
lst = [3,4,5,6,7]

sliced = lst[0:6:2]

print(sliced)
[3, 5, 7]

# reverse
lst = [3,4,5,6,7]

sliced = lst[::-1]

print(sliced)
[7,6,5,4,3]

# enumerate

lst = [-5,8,14]

for i, element in enumerate(lst):
    print(i, element)
    print(element * i)

0 -5
0
1 8
8
2 14
28

# set
s = {4,2,1}
print(s)
{1, 2, 4}

s.remove(4)
print(s)
{1, 2}

s = {4,2,1}
s.add(5)
print(s)
{1, 2, 4, 5}


s = {4,2,1}
s2 = {7,5}
print(s.union(s2))

{1, 2, 4, 5, 7}
s = {4,2,1}
s.add(5)
print(4 in s)
True

# dictionary
s = {'key':2}
del s['key']
print(s)
{}

x = {'key': 2}
for key, value in x.items():
    print(key, value)
key 2


x = {'key': 2}
for key in x:
    print(key)
key


# try-except
x = {'key': 2}
try:
    for key in y:
        print(key)
except Exception as e:
    print(e)
name 'y' is not defined

# lambda
x = lambda x: x + 5

print(x(2))
7

x = lambda x, y: x + y

print(x(2, 10))
12

# map
x = [1,2,4]

mp = map(lambda i: i+ 2, x)
print(list(mp))
[3, 4, 6]

# f'strings
x = f'hello {1 + 1} people'
print(x)
hello 2 people

y = 'all'
x = f'hello {y} people'
print(x)

hello all people


# Write a short Python function that takes a strings,representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam- ple,
# if given the string "Let s try, Mike.", this function would return "Lets try Mike".
def remove_punctuation(text):
  no_punct = ""
  for char in text:
    if char not in "!,;:.-?":
      no_punct += char
  return no_punct

# Example usage
text = "Let's try, Mike."
no_punct_text = remove_punctuation(text)
print(no_punct_text)  # Output: Lets try Mike

'''
Write three functions that take two strings, target and c (which will be a single character). The functions will count how many times c appears in target, returning the result.

char_count_while: Implements the character counting using a while loop.
char_count_for: Implements the character counting using a for loop (iterating over the string using indices (using range)).
char_count_foreach: Implements the character counting using a foreach loop (iterating over each character instead of using range).
'''


def char_count_while(target, c):
    count = 0
    index = 0
    while index < len(target):
        if target[index] == c:
            count += 1
        index += 1
    return count

def char_count_for(target, c):
    count = 0
    for i in range(len(target)):
        if c == target[i]:
            count += 1
    return count

def char_count_foreach(target, c):
    count = 0
    for letter in target:
        if c == letter:
            count += 1
    return count
        



target = "hello"
c = "l"

print(char_count_while(target, c))
print(char_count_for(target, c))
print(char_count_foreach(target, c))

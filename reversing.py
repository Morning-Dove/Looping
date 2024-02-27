def reverse_while(s):
    new_string = ""
    i = len(s)-1
    while i >= 0:
        new_string += s[i]
        i -= 1
    return new_string

def reverse_for(s):
    new_string = ""
    for i in range(len(s)-1, -1,-1):
        new_string += s[i]
    return new_string

def reverse_foreach(s):
    new_string = ""
    for letter in s[::-1]:
        new_string += letter
    return new_string



s = "hello world"   

print(reverse_while(s))
print(reverse_for(s))
print(reverse_foreach(s))



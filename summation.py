def summation_while(n): 
    number = 0
    i = 1
    while i <= n:
        number += i
        i += 1
    return number

def summation_for(n):
    number = 0
    for num in range(1, n+1):
        number += num
    return number

n = 5

print("while loop", summation_while(n))
print("for loop", summation_for(n))

        

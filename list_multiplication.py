def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    result = []
    i = 0
    while i < len(a):
        result.append(a[i]*b[i])
        i += 1
    return result
        

''' Implements the multiplication using a for loop (iterating over the items in the lists using indices (using range)).'''
def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    result = []
    for i in range(len(a)):
        result.append(a[i]*b[i])
    return result



a = [1, 2, 3]
b = [4, 5, 6]

print(list_multiply_while(a, b))  # This should compute [1*4, 2*5, 3*6]
print(list_multiply_for(a,b))  # Expected output: [4, 10, 18]

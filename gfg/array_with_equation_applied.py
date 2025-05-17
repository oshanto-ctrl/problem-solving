# Problem link:
def equationApplied(value, A, B, C):
    return A * pow(value, 2) + B * value + C

def sortArray(arr, A, B, C):
    arrAfterEquationApplied = []
    for value in arr:
        v = equationApplied(value, A, B, C)
        arrAfterEquationApplied.append(v)

    return sorted(arrAfterEquationApplied)


# Driver
# arr = [-3, -1, 2, 4]
# A = -1 
# B = 0
# C = 0

arr = [-4, -2, 0, 2, 4]
A = 1 
B = 3
C = 5
resultArray = sortArray(arr, A, B, C)
# Sort in ASC, Print
print(resultArray)

# Python3 implementation of left rotation
# of an array K number of times
 
# Fills temp with two copies of arr
def preProcess(arr, n):
    temp = [None] * (2*n)

    #storing arr elements at i and i+n
    for i in range(n):
        temp[i] = temp[i+n] = arr[i]
    return temp

def leftRotate(arr, n, k ,temp):
    # Starting position of array after k
    # rotations in temp will be k % n

    start = k % n
    #print array after k rotation
    for i in range(start, start+n):
        print(temp[i], end = " ")
    print("")

# driver program
arr = [1, 3, 5, 7, 9]
n = len(arr)
temp = preProcess(arr, n)

print(temp)

k = 2
leftRotate(arr, n , k , temp)

print(temp)

k = 3
leftRotate(arr, n , k , temp)

k = 4
leftRotate(arr, n , k , temp)

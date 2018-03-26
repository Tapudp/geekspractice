"""
    recursive implementation

"""
#arr = []
def leftRotate(arr, d, n):
    # Return if number of elements to be rotated is zero or equal to array size
    if(d == 0 or d == n):
        return
    # if number of elements to be rotated if exactly half of array size/
    if ( n - d == d):
        swap(arr, 0, n-d, d)
        return
    # if A is shorter
    if(d < n-d):
        swap(arr, 0, n-d, d)
        leftRotate(arr, d, n-d)
    else: # if B is shorter
        swap(arr, 0, d, n-d)
        leftRotate(arr+n-d, 2*d-n, d)

def printArray(arr, size):
    i = 0
    for i in range(size):
        print("%d"% arr[i], end=' ')
    print("\n")

def swap(arr, fi, si, d):
    i = 0
    #temp = list
    for i in range(d):
        arr[fi + i], arr[si+i] = arr[si + i], arr[fi+i]

# Driver program to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)


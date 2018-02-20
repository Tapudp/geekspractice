def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

# utility funciton to print an array
def printArray(arr, size):
    for i in range(size):
        print("%d"% arr[i], end=' ')

# driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
print("original array is: ")
for i in range(len(arr)):
    print("%d"% arr[i], end=' ')
leftRotate(arr, 2, 7)
print("\nRotated the array 2 at a time is:")
printArray(arr, 7)
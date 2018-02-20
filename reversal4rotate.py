# for reversal algorithm for array rotation

def reverseArray(arr, start, end):
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1

# function to rotate array of size n by d
def leftRotate(arr, d):
    n = len(arr)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

# function to print array
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')

#driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2) #Rotate by 2
printArray(arr)
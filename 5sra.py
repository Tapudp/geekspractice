"""
    Python3 program to find a pair with a given sum in a sorted and rotated array
"""
"""
this function returns true if arr[0..n-1] has a pair with sum equals to x.
"""
def pairInSortedRotated(arr, n, x):
    # Find the pivot element 
    for i in range(0, n-1):
        if(arr[i] > arr[i+1]):
            break
    #l is now index of minimum element
    l = (i+1)%n
    #r is now index of maximum element
    r = i
    # Keep moving either 1 or r till they meet
    while(l != r):
        #if we find a pair with sum x, we return the value
        if(arr[l] + arr[r] == x):
            return True
        
        #if current pair sum is less move to the higher one
        if(arr[i] + arr[r] < x):
            l = (l+1) % n
        else:
            # Move to the lower sum side
            r = (n+r - 1)%n

        return False

# Driver program to test above function
arr = [11, 15, 26, 38, 9, 1]
sum = 16
n = len(arr)
if(pairInSortedRotated(arr, n , sum)):
    print("Array has two elements with sum 16")
else: 
    print("Array doesn't have two elements with sum 16")
""" A naive Python 3 program to find maximum sum rotation"""

import sys

# Returns maximum value of i * arr[i]
def maxSum(arr, n):
    #initialize result
    res = -sys.maxsize

    # Consider rotation beginning with i for all possible values of i
    for i in range(0, n):
        # initialize sum of current rotation
        curr_sum = 0

        """Compute sum of all values. We don't actually rotate the array but compute the sum by finding the index when arr[i] is first element"""
        for j in range(0, n):
            index = int((i+j)% n)
            curr_sum += j * arr[index]

        # Updatae result if required
        res = max(res, curr_sum)

    return res

# Driver code
arr = [8, 3, 1, 2]
n = len(arr)

print(maxSum(arr, n))
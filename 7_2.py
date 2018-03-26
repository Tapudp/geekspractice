# an  efficient Python 3 program to compute maximum sum of i * arr[i]

def maxSum(arr, n):
    # Compute sum of all array elements
    cum_sum = 0

    for i in range(0, n):
        cum_sum += arr[i]

    # Compute sum for i * arr[i] for initial configuration
    curr_val = 0

    for i in range(0, n):
        curr_val += arr[i]

    # Initialize result
    res = curr_val

    #Compute value for other iterations
    for i in range(1, n):
        # Compute next value using previous value in O(1) time
        next_val = (curr_val - (cum_sum - arr[i-1]) + arr[i-1]*(n-1))

        #Update the current value
        curr_val = next_val
        # Update the result if required 
        res = max(res, next_val)

    return res

# Driver code
arr = [8, 3, 1, 2]
n = len(arr)
print(maxSum(arr, n))

# 1. Maximum sum of a subarray of size k

def max_sub_array_of_size_k(k, arr):
    low = 0
    sum = 0
    result = 0

    for high in range(len(arr)):
        sum += arr[high]

        # window size becomes k
        if high >= k - 1:
            result = max(result, sum)

            # slide window
            sum -= arr[low]
            low += 1

    return result

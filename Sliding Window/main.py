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

# 2. Minimum size subarray sum 

def smallest_sub_array_sum(s, arr):
    low = 0
    total = 0
    answer = float('inf')

    for high in range(len(arr)):
        total += arr[high]

        while total >= s:
            length = high - low + 1
            answer = min(answer, length)

            total -= arr[low]
            low += 1

    if answer == float('inf'):
        return 0

    return answer

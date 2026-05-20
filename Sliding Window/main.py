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

# 3. Longest substring with k distinct characters

def longest_substring_with_k_distinct(s, k):
    low = 0
    freq = {}
    answer = 0

    for high in range(len(s)):
        ch = s[high]

        # add character
        freq[ch] = freq.get(ch, 0) + 1

        # shrink window if distinct chars > k
        while len(freq) > k:
            left_char = s[low]
            freq[left_char] -= 1

            if freq[left_char] == 0:
                del freq[left_char]

            low += 1

        # update maximum length
        answer = max(answer, high - low + 1)

    return answer


# 4. Fruits into baskets   

def total_fruit(tree):
    left = 0
    fruits = {}
    max_fruits = 0

    for right in range(len(tree)):

        # add current fruit
        fruit = tree[right]
        fruits[fruit] = fruits.get(fruit, 0) + 1

        # if more than 2 fruit types, shrink window
        while len(fruits) > 2:
            left_fruit = tree[left]

            fruits[left_fruit] -= 1

            # remove fruit if count becomes 0
            if fruits[left_fruit] == 0:
                del fruits[left_fruit]

            left += 1

        # store maximum window size
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


# 5. No-repeat substring

def length_of_longest_substring(s):
    low = 0
    freq = {}
    answer = 0

    for high in range(len(s)):
        ch = s[high]

        # add character
        freq[ch] = freq.get(ch, 0) + 1

        # shrink window if character repeats
        while freq[ch] > 1:
            left_char = s[low]
            freq[left_char] -= 1

            if freq[left_char] == 0:
                del freq[left_char]

            low += 1

        # update maximum length
        answer = max(answer, high - low + 1)

    return answer
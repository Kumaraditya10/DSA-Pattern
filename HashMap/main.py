# 1. First non-repeating character

def first_non_repeating_character(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


# 2. Maximum number of Balloons

def max_number_of_balloons(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    count = float('inf')

    for ch in 'balloon':
        count = min(count, freq.get(ch, 0))

    # 'l' and 'o' are repeated twice in 'balloon'
    count //= 2

    return count 

# 3. Longest Palindrome

def longest_palindrome(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    length = 0
    odd_count = 0

    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_count += 1

    # we can use one odd character in the middle of the palindrome
    if odd_count > 0:
        length += 1

    return length
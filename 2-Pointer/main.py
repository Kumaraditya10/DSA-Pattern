# 1. Two Sum II - Input Array Is Sorted

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []  # Return an empty list if no solution is found


# 2. Remove Duplicates from Sorted Array

def remove_duplicates(nums):
    if not nums:
        return 0

    write_index = 1

    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index  # Return the new length of the array without duplicates


# 3. Squares of a Sorted Array

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1

        index -= 1

    return result
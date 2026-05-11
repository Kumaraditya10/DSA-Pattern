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
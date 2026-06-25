#Write functions to find maximum and minimum in a list without using built-in max()/min().
def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum
nums = [77, 7, 19, 45, 67]
max_val, min_val = find_max_min(nums)
print("Maximum:", max_val)
print("Minimum:", min_val)
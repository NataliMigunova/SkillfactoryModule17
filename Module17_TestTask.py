import re


def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return arr[high]


def validate_inputs(numbers_list_string, control_number_string):
    if not re.match("^[0-9 ]+$", numbers_list_string):
        print("ERROR: Please type squence numbers separated by space")
        quit()
    if not re.match("^[0-9]+$", control_number_string):
        print("ERROR: Please type only digits for control number")
        quit()


numbers_list_string = input("Please, enter number sequence divided by ',':")
control_number_string = input("Please, enter control number:")

validate_inputs(numbers_list_string, control_number_string)

numbers_list = []

control_number = int(control_number_string)

for num_str in numbers_list_string.split(' '):
    numbers_list.append(int(num_str))

sorted_list = merge_sort(numbers_list)
print ("Sorted numbers - {}".format(sorted_list))

print("Control number position - {}".format(binary_search(sorted_list, 0, len(sorted_list)-1, control_number)))

def mergesort(my_array):
    if len(my_array) <= 1:
        return my_array
    mid = len(my_array) // 2
    left = my_array[:mid]
    right = my_array[mid:]

    sorted_left = mergesort(left)
    sorted_right = mergesort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

array = [8, 6, 3, 7, 5, 6, 1, 4, 9]
print(mergesort(array))
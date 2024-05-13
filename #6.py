
def deleteElement(arr, index):
    if index < 0 or index >= len(arr):
        return "Invalid syntax", arr  # Invalid index, return the original array unchanged
    arr[index], arr[-1] = arr[-1], arr[index]  # Swap with the last element
    arr.pop()  # Remove the last element
    return arr
array=[3, 7, 1, 9, 4]
print(deleteElement(array,9))




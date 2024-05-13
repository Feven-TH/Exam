def linear(arr, target):
    occurrence = 0
    for i in range(len(arr)):
        if arr[i] == target:
            occurrence += 1
    if occurrence == 0:
        return "not found"
    else:
        return occurrence
array= [8,6,3,7,5,6,1,4,9]
my_target = int(input('Enter the target number: '))
print(linear(array,my_target))


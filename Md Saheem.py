arr = []

print("Enter 10 numbers:")

# Input 10 numbers
for i in range(10):
    num = int(input())
    arr.append(num)

# Bubble Sort
for i in range(9):
    for j in range(9 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted numbers:")
for i in range(10):
    print(arr[i], end=" ")

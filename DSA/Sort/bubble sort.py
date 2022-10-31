a = arr = []
size = int(input("Enter size of array : "))

for i in range(0, size):
    a.append(int(input(f"Enter element {i+1} : ")))

for i in range(1, size):
    for j in range(0, size-i):
        if arr[j] > arr[j+1]:
            swap = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = swap
print(arr)




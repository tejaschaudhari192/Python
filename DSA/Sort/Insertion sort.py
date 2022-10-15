n = int(input("Enter Length of array : "))

a=[]

for i in range(0,n):
    a.append(int(input(f"Enter {i}th element : ")))

print(f"Entered list {a}")

for k in range(1,len(a)):
    j= k-1
    temp = a[k]

    while j>=0 and temp <= a[j]:
        a[j+1]=a[j]
        j-=1

    a[j+1]=temp
    

print(f"Sorted list {a}")
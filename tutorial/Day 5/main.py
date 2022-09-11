from itertools import count
from posixpath import split

height = input("Enter height of students : ").split()

count=0
tot = 0

for h in height:
    height[count]=int(height[count])
    count= count + 1
    tot = tot + height[count]

print(count)
print(tot)

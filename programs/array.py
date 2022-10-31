z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
l = len(z)
a = []
b = []
new = []
div = l//2

for i in range(0, div):
    a.append(z[i])

for j in range(div, l):
    b.append(z[j])

for k in range(0, div):
    new.append(a[k])
    new.append(b[k])

print(new)

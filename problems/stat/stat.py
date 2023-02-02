import statistics as st

x = []
y = []
for i in range(10):
    x.append(int(input()))
print(x)
for i in range(10):
    y.append(int(input()))
# print(y)
# z = []
# for i in range(len(x)):
#     z.append(x[i] - y[i])
# print(z)
print(st.mean(x))
print(st.stdev(x))

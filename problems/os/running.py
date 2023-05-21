arr = input().split(' ')
run = [];sum = 0
for i in arr:
    sum += int(i)
    run.append(sum)
print(run)
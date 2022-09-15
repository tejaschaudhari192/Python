from operator import length_hint


wordlist = ["banana", "bhoju"]

choosed = wordlist[0]
print(choosed[1])

c = input("Enter char : ")

clist = []
i = 0

for index in range(0, len(choosed)):
    clist.append(choosed[index])

print(clist)

while i < len(clist):
    if c == clist[i]:
        print("yes")
    else:
        print("no")
    i += 1

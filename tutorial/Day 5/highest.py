from itertools import count

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
n = 0
for score in student_scores:
    if score > max:
        max = score

print(max)

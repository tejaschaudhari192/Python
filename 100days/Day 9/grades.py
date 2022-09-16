student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
grade=""
for stud in student_scores:
    if int(student_scores[stud])>=91 :
        grade="Outstanding"
    elif int(student_scores[stud])>=81 :
        grade="Exceeds Expectations"
    elif int(student_scores[stud])>=71 :
        grade="Acceptable"
    else:
        grade="Fail"

    
    student_grades[stud]= grade

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)
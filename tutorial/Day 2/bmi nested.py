height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float(weight)/(float(height**2))


if bmi < 18.5:
    print(f"Your BMI is {round(bmi,2)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi,2)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi,2)}, you are slightly overweight.")
else:
    print(f"Your BMI is {round(bmi,2)}, you are clinically obese.")

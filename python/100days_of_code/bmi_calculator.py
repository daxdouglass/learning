print("Welcome to the BMI calculator!")

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in lbs: "))

bmi = 703 * (weight / (height ** 2))

print("Your BMI is: ", str(round(bmi, 2)))

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")

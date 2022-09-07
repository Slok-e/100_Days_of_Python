# Starter code

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Your ticket is $5.")
    elif age > 12 or age <= 18:
        print("Your ticket is $7")
    else:
        print("Your ticket is $12")
else:
    print("Sorry, you're not tall enough.")


















#     # BMI Calculator

# # User Input
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# #Calculation
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
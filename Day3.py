# Starter code

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print(f"CHild tickets are $5.")
    elif age <= 18:
        bill = 7
        print(f"Teen tickets are $7")
    elif age >= 45 and age <=55:
        print("The ride is on us!!")
    else:
        bill = 12
        print(f"Adult tickets are  $12")
    photo = input("Do you want a photo to taken? Press Y for 'yes' and N for 'no'")
    if photo == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")
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
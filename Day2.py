# Todays project is a tip calculator this will be comprised of the Data Types we learned.

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total_bill = float(input("What is your bills total? "))

tip = float(input("Whats percent tip would you like to add? ")) / 100 + 1

bill_split = int(input("How man people will be splitting the bill? "))

total_per_person = total_bill * tip / bill_split

print(f"Each person should pay ${round(total_per_person, 2)}")
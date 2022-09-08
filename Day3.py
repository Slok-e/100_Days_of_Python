# Starter code
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You enter the maze from the treasure map that you found in your attic and you come to a split hall way.")
choice_1 = input("Choose to go left or right. (Type 'Left' or 'Right'.").lower()
if choice_1 == "left":
    choice_2 = int(input('''After a short walk you come to a large ballroom with chandeliers, but its dark. You see a power box with its lever
    down. Pull the lever up? or find another light source? Type '1' for lever or '2' for other source.'''))
    if choice_2 == 2:
        print('''After taking a second thought about just willy nilly pulling the lever up. You remember your first lesson in 
        treasure hunting where booby traps are attached to important necessities. You look around and see a cabinet to the 
        left of the lever and open it; there is a flashlight in there and as soon as you pick it up the back of the the cabinet falls out.''')
        input("(Do you '1' go in?!) or ('2' back out and look around some more?)")
else:
    print('''You come down a long corridor that is seemingly endless only to find youve walked yourself into exhaustion
    and the room keeps going as it slowly gets pitch black and you die after years in darkness.
    
    ................... The end. ''')
print(choice_2)


















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
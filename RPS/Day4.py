import random

# RPS Choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock, Paper, Scissors as a list
rps = [rock, paper, scissors]

#User Choice
choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
pc_choice = random.choice(rps)
if choice == 0 and pc_choice == rps[0]:
    print(f"You chose Rock{rps[choice]}\n Your opponent chose Rock{pc_choice}\n")
    print("It's a Draw")
if choice == 1 and pc_choice == rps[1]:
    print(f"You chose Paper{rps[choice]}\n Your opponent chose Paper{pc_choice}.\n")
    print("It's a Draw")
if choice == 2 and pc_choice == rps[2]:
    print(f"You chose Scissors{rps[choice]}\n Your opponent chose Scissors{pc_choice}.\n")
    print("It's a Draw")
if choice == 0 and pc_choice == rps[1]:
    print(f"You chose Rock{rps[choice]}\n Your opponent chose Paper{pc_choice}.\n")
    print("You Lose")
if choice == 0 and pc_choice == rps[2]:
    print(f"You chose Rock{rps[choice]}\n Your opponent chose Scissor{pc_choice}.\n")
    print("You Win!")
if choice == 1 and pc_choice == rps[0]:
    print(f"You chose Paper{rps[choice]}\n Your opponent chose Rock{pc_choice}.\n")
    print("You Win!")
if choice == 1 and pc_choice == rps[2]:
    print(f"You chose Paper{rps[choice]}\n Your opponent chose Scissors{pc_choice}.\n")
    print("You lose")
if choice == 2 and pc_choice == rps[0]:
    print(f"You chose Scissors{rps[choice]}\n Your opponent chose Rock{pc_choice}.\n")
    print("You lose")
if choice == 2 and pc_choice == rps[1]:
    print(f"You chose Scissors{rps[choice]}\n Your opponent chose Paper{pc_choice}.\n")
    print("You Win!")
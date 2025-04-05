import random

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

rps = [rock, paper, scissors]
choice = input("Rock, paper, or scissors? ").lower()
rand = random.randint(0, len(rps) - 1)
randChoice = ""

print("You chose:")

if choice == "rock":
    print(rock)
elif choice == "paper":
    print(paper)
else:
    print(scissors)

print("Opponent chose:")

if rand == 0:
    print(rock)
    randChoice = "rock"
elif rand == 1:
    print(paper)
    randChoice = "paper"
else:
    print(scissors)
    randChoice = "scissors"

if (choice == "rock" and randChoice == "paper") or (choice == "paper" and randChoice == "rock") or (choice == "scissor" and randChoice == "rock"):
    print("You win")
elif choice == randChoice:
    print("Tie")
else:
    print("You lose")
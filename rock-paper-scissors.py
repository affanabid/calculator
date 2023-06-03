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
images = [rock, paper, scissors]
endgame = False
while not endgame:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user >= 3 or user < 0:
        print("You entered an invalid number!")
    else:
        print("You chose: ")
        print(images[user])

        computer = random.randint(0, 2)
        print("Computer chose: ")
        print(images[computer])

        if computer == 0 and user == 2:
            print("you lose!")
        elif user == 0 and computer == 2:
            print("you win!")
        elif user > computer:
            print("you win!")
        elif computer > user:
            print("you lose!")
        elif user == computer:
            print("Draw!")



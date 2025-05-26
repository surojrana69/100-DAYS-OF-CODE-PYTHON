from http.cookiejar import user_domain_match

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

import random

game_images = [rock, paper, scissors]

User_Choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("Your choice:")
# if User_Choice==0:
#     print(rock)
# elif User_Choice==1:
#     print(paper)
#
# elif User_Choice==2:
#     print(scissors)
if User_Choice >= 0 or User_Choice <2:
    print(game_images[User_Choice])

else:
     print("Dumb!")

print("Computer Choose:")
Computer_Choice=random.randint(0,2)
print(game_images[Computer_Choice])
# if Computer_Choice==0:
#     print(rock)
# elif Computer_Choice==1:
#     print(paper)
#
# elif Computer_Choice==2:
#     print(scissors)

if User_Choice==0 and Computer_Choice==1:
    print("You loose!")
elif User_Choice==1 and Computer_Choice==0:
    print("You won!")
elif User_Choice==2 and Computer_Choice==0:
    print("You loose!")
elif User_Choice==0 and Computer_Choice==2:
    print("You won!")
elif User_Choice==2 and Computer_Choice==1:
    print("You won!")
elif User_Choice==1 and Computer_Choice==2:
    print("You loose!")
else:
    print("Draw")
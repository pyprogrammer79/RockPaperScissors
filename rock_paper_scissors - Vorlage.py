import random

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ___)____
          ______)
       __________)
      (___)
---.__(___)
"""
print("=========================================")
print("          Rock Paper Scissors")
print("========================================= \n")
print("Der beste aus 3 gewinnt! \n")
user_points=0
pc_points=0

for i in range(3):
    user=int(input("Wähle [0] für Stein, [1] für Papier, [2] für Schere:"))
    zufall=random.randint(0,2)
    if user==0:
        print(f"Du wählst: \n", rock)
    elif user==1:
        print(f"Du wählst: \n", paper)
    elif user==2:
        print(f"Du wählst: \n", scissors)
    
    if zufall==0:
        print(f"PC wählt: \n", rock)
    elif zufall==1:
        print(f"PC wählt: \n", paper)
    elif zufall==2:
        print(f"PC wählt: \n", scissors)

    if user==0 and zufall==1:
        print("Du hast verloren \n")
        pc_points+=1
    elif user==0 and zufall==2:
        print("Du hast gewonnen \n")
        user_points+=1
    elif user==1 and zufall==0:
        print("Du hast gewonnen \n")
        user_points+=1
    elif user==1 and zufall==2:
        print("Du hast verloren \n")
        pc_points+=1
    elif user==2 and zufall==0:
        print("Du hast verloren \n")
        pc_points+=1
    elif user==2 and zufall==1:
        print("Du hast gewonnen \n")
        user_points+=1
    elif user!=0 and user!=1 and user!=2:
        print("Falsche Eingabe")
        break
    else:
        print("Unentschieden! \n")
    
    print(f"Deine Punkte: {user_points}, Punkte vom PC: {pc_points} \n")

if user_points>pc_points:
    print("Herzlichen Glückwunsch! Du hast gewonnen!")
elif user_points<pc_points:
    print("Du hast leider gegen den PC verloren")
elif user_points==pc_points:
    print("Unentschieden!")
   
# #   1 for snake
# #  -1 for water
# #   0 for gun

# import random
# computer = random.choice([1,-1,0])
# youstr = input("ENTER YOUR CHOICE :")
# youDict ={"s":1, "w":-1, "g":0}
# you = youDict[youstr]

# reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}

# print(f"YOU CHOSE {reverseDict[you]}\nCOMPUTER CHOSE {reverseDict[computer]}")

# if(computer == you):
#     print("IT'S A DRAW")

# else:
#     if(computer == -1 and you == 1):
#         print("YOU WIN!")

#     elif(computer == -1 and you == 0):
#         print("YOU LOSE!")
    
#     elif(computer == 1 and you == -1):
#         print("YOU LOSE!")   

#     elif(computer == 1 and you == 0):
#         print("YOU WIN!")   

#     elif(computer == 0 and you == -1):
#         print("YOU WIN!") 
  
#     elif(computer == 0 and you == 1):
#         print("YOU LOSE!")  

#     else:
#         print("SOMETHING WENT WRONG")

   

#        # IN SHORT FORM


# # if((computer - you) == -1 or (computer - you) == 2):
# #     print("YOU LOSE!")
# # else:
# #     print("YOU WIN!")


# ----------------------------
# SNAKE - WATER - GUN GAME
# MINI PROJECT (PYTHON)
# ----------------------------

import random
import time

# Dictionaries
choice_map = {"s": 1, "w": -1, "g": 0}
reverse_map = {1: "Snake", -1: "Water", 0: "Gun"}

def rules():
    print("\n----- GAME RULES -----")
    print(" Snake  vs Water → Snake drinks water → Snake Wins")
    print(" Snake  vs Gun   → Gun kills snake → Gun Wins")
    print(" Water  vs Gun   → Gun sinks in water → Water Wins")
    print("----------------------\n")

def play_round():
    computer = random.choice([1, -1, 0])
    
    you_str = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

    if you_str not in choice_map:
        print("\nInvalid choice! Please use s/w/g only.\n")
        return None  # Invalid round
    
    you = choice_map[you_str]

    print(f"\nYou chose     : {reverse_map[you]}")
    print(f"Computer chose: {reverse_map[computer]}\n")

    if computer == you:
        print("Result: It's a DRAW!\n")
        return "draw"

    # Win/Lose logic
    if (computer - you == -1) or (computer - you == 2):
        print("Result: YOU LOSE!\n")
        return "lose"
    else:
        print("Result: YOU WIN!\n")
        return "win"

def play_game():
    print("\nStarting 3-Round Match...\n")
    user_score = 0
    computer_score = 0

    for round_no in range(1, 4):
        print(f"------ Round {round_no} ------")
        result = play_round()

        if result == None:
            continue
        elif result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        time.sleep(0.5)

    # Final Result
    print("\n------ FINAL RESULT ------")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")

    if user_score > computer_score:
        print("\n🎉 YOU WON THE MATCH! 🎉\n")
    elif computer_score > user_score:
        print("\n💀 YOU LOST THE MATCH! 💀\n")
    else:
        print("\n😐 MATCH DRAW! 😐\n")

def main_menu():
    while True:
        print("========== SNAKE - WATER - GUN GAME ==========")
        print("1. Play Game")
        print("2. Rules")
        print("3. Exit")
        print("==============================================")

        ch = input("Enter your choice: ")

        if ch == "1":
            play_game()
        elif ch == "2":
            rules()
        elif ch == "3":
            print("\nThanks for playing! Goodbye.\n")
            break
        else:
            print("\nInvalid option! Please choose 1 / 2 / 3.\n")

# Run the game
main_menu()

import random
u=c=0
while True:
    user_action = input("Enter a choice (rock, paper, scissor): ")
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)
    
    print("\nYou chose ",user_action," computer chose ",computer_action,".\n")
    if user_action == computer_action:
        print("Both players selected ",user_action,". It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("Rock smashes scissor! You win!")
            u+=1
        else:
            print("Paper covers rock! You lose.")
            c+=1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            u+=1
        else:
            print("Scissors cuts paper! You lose.")
            c+=1
    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            u+=1
        else:
            print("Rock smashes scissor! You lose.")
            c+=1
    print("\tYour Score\t\tComputer Score")
    print("\t    ",u,"\t\t\t     ",c)
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
    

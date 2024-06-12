import os
def get_guess():
    guess = input("Enter your guess : ")
    while len(guess)!=4 or not guess.isdigit():
        guess=input("Invalid guess. Enter a 4-digit number :")
    return guess
def check_guess(number,guess):
    correct_digit=0
    correct_numbers=0
    for i in range(4):
        if guess[i]==number[i]:
            correct_digit+=1
        if guess[i] in number:
            correct_numbers+=1
    return correct_digit,correct_numbers
def play_game(player):
    tries=0
    while True:
        guess=get_guess()
        tries+=1
        correct_digit,correct_numbers = check_guess(number,guess)
        if correct_digit==4:
            os.system('cls')
            print(player,"guess the number in",tries,"tries")
            break
        else:
            print(player,"got",correct_digit,"correct digits and",correct_numbers,"correct numbers.")
    return tries
print("\t-----------------------------------------------")
print("\tPlay the Mastermind game between two players.")
print("\tGuess the 4 digit number and win")
print("\t-----------------------------------------------")
player1=input("\tEnter the name of Player 1: ")
player2=input("\tEnter the name of Player 2: ")

print("\n\n\t", player1 , "set the number.")
number= input("\tEnter the number: ")
os.system('cls')
p2tries=play_game(player2)
if p2tries==1:
    print(player2, "wins. He is Mastermind!")
    exit(0)

print("\tNow",player2,"set the number.")
number=input("\tEnter the number: ")
os.system('cls')
p1tries=play_game(player1)

if p1tries<p2tries:
    print(player1,"wins")
else:
    print(player2,"wins")
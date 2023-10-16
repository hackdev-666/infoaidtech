from random import *
def number_guessing_game():
    while True:
        num=randint(0, 100)
        a=0
        m=10
        print("I'm thinking of a number between 0 and 100. Try to guess it....")
        print(f"You have {m} attempts.")
        while a<m:
            try:
                guess=int(input("Enter your guess: "))
                a+=1
                if guess<num:
                    print("Higher! Try again.")
                elif guess>num:
                    print("Lower! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {num}.")
                    break
            except ValueError:
                print("Please enter a valid number.")
        if a == m:
            print(f"Sorry, you've used all {m} attempts. The secret number was {num}.")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower()!="yes":
            break
if __name__ == "__main__":
    number_guessing_game()

 






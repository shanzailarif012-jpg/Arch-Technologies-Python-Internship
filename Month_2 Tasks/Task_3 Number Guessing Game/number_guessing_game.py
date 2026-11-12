# Number Guessing Game By Dev_Shanzail 
import random

def get_user_guess():
    while True:
        user = input("Please Enter a Number: ")
        try:
            number_convert = int(user)
            if number_convert in range(1,101):
                return number_convert
            else:
                print("Enter a number between 1 to 100")
        except ValueError:
            print("Invalid input, enter digit only")


def play_game():
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts = attempts + 1

        if guess > secret:
            print("Too High")
        elif guess < secret:
            print("Too Low")
        else:
            print(f"Correct! You guessed in {attempts} attempts")
            break


def main():
    print("Welcome Number Guessing Game")
    while True:
        play_game()
        choice =input("Play Again?? (yes/no): ").strip().lower()
        if choice == ("no"):
            break
    print("GoodBye")

if __name__ == "__main__":
    main()
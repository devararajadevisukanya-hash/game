import random

best_score = None

while True:
    print("\n===== NUMBER GUESSING GAME =====")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")

    choice = input("Choose difficulty of the game: ")

    if choice == "1":
        maximum = 10
    elif choice == "2":
        maximum = 50
    elif choice == "3":
        maximum = 100
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
        continue

    secret_number = random.randint(1, maximum)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {maximum}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Higher! Try again.")
            elif guess > secret_number:
                print("Lower! Try again.")
            else:
                print(f"Correct! You found the number in {attempts} attempts.")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print(" New best score!")

                print(f"Best score: {best_score} attempts")
                break

        except ValueError:
            print("Please enter a valid number.")

    replay = input("\n Do you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("Thanks for playing!")
        break
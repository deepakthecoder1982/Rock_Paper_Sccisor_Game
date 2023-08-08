import random

user_wins = 0
computer_wins = 0
draws = 0


def start():
    global user_wins, computer_wins, draws
    choices = ["Rock", "Paper", "Scissor"]
    print("------------------------------")
    print("Let's play Rock Paper & Scissor")
    print("Choose from the options:")
    print("0) Rock")
    print("1) Paper")
    print("2) Scissor")
    print("------------------------------")

    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice in range(3):
            user_choice = choices[user_choice]
            computer_choice = random.choice(choices)
            print("User's Choice:", user_choice)
            print("Computer's Choice:", computer_choice)

            if user_choice == computer_choice:
                draws += 1
                print("There is a draw")
            elif (user_choice == choices[0] and computer_choice == choices[2]) or \
                 (user_choice == choices[1] and computer_choice == choices[0]) or \
                 (user_choice == choices[2] and computer_choice == choices[1]):
                print("User wins")
                user_wins += 1
            else:
                print("Computer wins")
                computer_wins += 1

            result(user_wins, computer_wins, draws)
        else:
            print("Please enter a valid choice (0, 1, or 2).")
            start(user_wins, computer_wins, draws)
    except ValueError:
        print("Please enter a valid choice (0, 1, or 2).")
        start()


def result(user_wins, computer_wins, draws):
    print("=======================================================")
    print(
        f"Final Score:\nComputer: {computer_wins}\nUser: {user_wins}\nDraws: {draws}"
    )
    print("=======================================================")
    play_another = input("Want to play another round? (yes/no): ")
    try:
        if play_another.lower() == "no":
            print("Thank you for playing! See you soon 👍👍🏼")
        else:
            start()
    except ValueError:
        print("Please Enter the valid input: \n")
        result(user_wins, computer_wins, draws)


start()

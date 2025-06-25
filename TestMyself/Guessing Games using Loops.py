def num_game():
    limit = 0

    while limit < 5:
        secret_num = int(input("Enter secret number: "))
        limit += 1
        
        if secret_num == 25:
            print("Correct!")
            break
        elif secret_num >= 100:
            print("Too High!")
        elif secret_num <= 0:
            print("Too Low!")
        else:
            print("Wrong Number!")

    if limit == 5 and secret_num != 25:
        print("Out of guesses1 The secret number was 25" )
        
    
def password():
    pw = ""
    limit = 0

    while limit < 5:
        pw = input("Enter Your Password: ")
        limit+=1

        if pw == "Dell":
            print("Logging In...")
            break
        else:
            print("Wrorng Password, try again!")

    if limit == 5 and pw != "Dell":
        print("Refresh To reset device")

game_choice = input("Do you want to play a game? (Enter y=yes or n=no.) ")

if game_choice == "y":
    game_names = input("Enter 1 = Numbers or 2 = Password: ")

    if game_names == "1":
        num_game()
    elif game_names == "2":
        password()
    else:
        print("Invalid. Please press 1 or 2")
elif game_choice == "n":
    print("Goodbye")
else:
    print("invalid")

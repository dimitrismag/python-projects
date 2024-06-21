import random

play = input("Would you like to play? ")
if play.lower() != "yes":
    quit()
print("Lets go")
def user_guess_is():

    while True:
        pick = input("Pick a number between 1 and 10: ")
        if pick.isnumeric():
            pick = int(pick)
            if 1 <= pick <= 10:
               return pick
            else:
                print("Sorry, that number must be between 1 and 10")
        else:
            print("sorry this is not an integer")


def main():
    random_guess = random.randint(1, 10)
    while True:
        if random_guess == user_guess_is():
            print("You got it!")
            break
        else:
            print("Sorry, you didnt get it!")

if __name__ == "__main__":
    main()






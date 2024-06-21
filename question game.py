print("Welcome to Question Quiz!")
play = input("Do you want to play? ")
if play.lower() == "yes":
    print("Okay Lets start!")
else:
    quit()

score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your score is", score, "correct answers")
print("Your percentage is", (score/4)*100,"%")

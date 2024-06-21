import random
import time

OPERATORS = ['+', '-', '*']
MAX_OPERATOR = 15
MIN_OPERATOR = 1
PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    operator = random.choice(OPERATORS)

    expr = str(left) + "" + operator + "" + str(right)
    answer = eval(expr)
    return expr, answer

mistakes = 0
input("press anykey to start")
start_time = time.time()

for i in range(PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + "= ")
        if guess == str(answer):
            break
        mistakes += 1
end_time = time.time()
print("Time taken: " + str(round((end_time - start_time),2)) + " seconds " + "you did: " + str(mistakes) + " wrong guesses")
print('Good Work!!')

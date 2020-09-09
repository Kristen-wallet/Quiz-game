score = 0
def check(guess,answer):
    global score
    attempt = 0
    still_guessing=True
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Answer not matching..Try again ")
            attempt = attempt+1

    if attempt == 3:
        print("correct answer is "+answer)

print("Welcome to the guessing game")
guess = input("Which is the fastest animal?")
check(guess,"cheetah")
guess = input("Which is the tallest animal?")
check(guess,"giraffe")
guess = input("Which is the biggest animal?")
check(guess,"whale")

print("Score = "+str(score))
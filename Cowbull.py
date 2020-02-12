import random


def determine(num, guess):
    cowbull = [0, 0]
    #num = str(num)
    #guess = str(guess)
    for i in range(4):
        if num[i] == guess[i]:
            cowbull[0] += 1                             #cow++
        else:
            for k in range(4):
                if guess[i] == num[k] and k != i:
                    cowbull[1] += 1                     #bull++
                    #break
    return cowbull


if __name__ == '__main__':
    num = random.randrange(1000, 9999)
    print("Cows and Bulls")
    print("--------------")
    print("Instructions: \n\nEnter a 4 digit number. "
          "If the number guessed has x amount of correct \n"
          "digits in the correct place, then you will have "
          "x cows. If the number guessed has y amount of \n"
          "correct digits in the wrong place, then you will "
          "y bulls. A cow cannot count as a bull, so if the \n"
          "number is 1211, and you guess 1333, you will "
          "recieve 1 cow, 0 bulls.\n")
    print("Random 4 digit number has been generated.")
    print(num)

    numGuess = 0
    guess = raw_input("Guess the number: ")
    if str(guess) == "exit":
        print("You didn't even try. I am thankful I am a computer and not a disgraceful chimp...")
        exit()
    cowbull = [0, 0]
    numGuess = 1

    while str(guess) != str(num):
        if str(guess) == "exit":
            print("You are a failure and it took you " + str(numGuess) + " guesses to figure it out.")
            print("The number was " + str(num))
            exit()

        while len(str(guess)) != 4:
            guess = raw_input("Invalid number. PLease enter a valid number: ")

        cowbull = determine(str(num), str(guess))
        print(str(cowbull[0]) + " cows, " + str(cowbull[1]) + " bulls.")
        guess = raw_input("Guess the number: ")
        numGuess += 1

    print("4 cows. It only took " + str(numGuess) + " guesses.")


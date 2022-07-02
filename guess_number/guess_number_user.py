import random 

def function_pass():
    pass

#returns a random number
def produce_random_number_between_one_and(limit):

    random_number = random.randint(1, limit)
    return random_number




#now we have to guess the random number
def now_lets_guess_the_number(random_number, limit):

    number_to_be_guessed = random_number
    our_guess = 0 #initializing our guess number 

    while our_guess != number_to_be_guessed:
        our_guess = int(input(f"Please guess a number between 1 and {limit}: "))

        if our_guess < number_to_be_guessed:
            print("Sorry guess again, too low: ")
        elif our_guess > number_to_be_guessed:
            print("Sorry guess again, too high: ")

    print("CORRECT!!!")
    print("\n", number_to_be_guessed)



def main():
    print("\nProgram Started!!! \n")

    print("This is a game in which the user has to guess the number.\n\nUser has to guess the number between 1 and the upper limit number. \n")

    limit = int(input("Please enter the upper limit number "))

    random_number = produce_random_number_between_one_and(limit)

    now_lets_guess_the_number(random_number, limit)



if __name__ == "__main__":
    main()






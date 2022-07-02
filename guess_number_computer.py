import random


#returns a random number
def produce_random_number_between(lower_limit, upper_limit):
    random_number = random.randint(lower_limit, upper_limit)
    return random_number
   


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#recursive method for the computer to guess the number

""" how it works: lets say the interval is (1,10)
    with lower_limit = 1 and upper_limit = 10
    and the number is 7
    1st computer_guess lets say it will be 3
    so computer_guess = 3
    , 3 is the wrong number
    so now the computer has to guess something higher,
    the lower_limit = computer_guess + 1, the upper_limit remains the same 
    and the new interval will be (4,10), the method then calles itself and 
    the computer tries again to guess
    
    another example with the same interval (1,10) and number 3 
    1st computer_guess will be 6, 
    so computer_guess = 6,
    6 is higher than 3 so now the computer
    has to guess something smaller, the upper_limit = computer_guess - 1
    and the new interval now is (1,5), the method then calles itself and 
    the computer tries again to guess """
def now_let_the_computer_guess_the_number(lower_limit, upper_limit, user_input,random_number):

    if random_number == user_input:
        return random_number


    elif random_number > user_input:
        print(f"Sorry,{random_number} is too big, try smt smaller!!")

        #narrowing down the interval
        upper_limit = random_number - 1 

        #and producing a new number in the new interval 
        random_number = produce_random_number_between(lower_limit, upper_limit) 
        return now_let_the_computer_guess_the_number(lower_limit, upper_limit, user_input, random_number)
    elif random_number < user_input:
        print(f"Sorry,{random_number} is too low, try smt bigger!!")
        lower_limit = random_number + 1 #narrowing down the interval 
                                        #and producing a new number in the new interval
        random_number = produce_random_number_between(lower_limit, upper_limit) 
        return now_let_the_computer_guess_the_number(lower_limit, upper_limit, user_input, random_number)

         


    

   


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#returns true if the user input is in the interval of numbers 
def check_if_user_input_is_in_the_interval(lower_limit, upper_limit, user_input):

    if user_input <=upper_limit and user_input>=lower_limit:
        return True

    return False 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# returns true if upper limit of the interval > lower limit 
def check_interval(lower_limit, upper_limit):

    if lower_limit<upper_limit:
        return True

    return False


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  
    

def main():


    print("\nProgram Started!!! \n")



    print("This is a game in which the computer has to guess the number.\n\nComputer has to guess the number between lower limit and the upper limit number. \n")



    lower_limit = int(input("Please enter the lower limit of the interval:  "))
    upper_limit = int(input("\nPlease enter the upper limit of the interval: "))



    while check_interval(lower_limit, upper_limit) is not True:


        print("Please enter a valid interval: ")


        lower_limit = int(input("\nPlease enter the lower limit of the interval:  "))
        upper_limit = int(input("\nPlease enter the upper limit of the interval: "))


        #end while



    user_input = int(input("\nPlease enter the number to be guessed by the computer: "))



    while check_if_user_input_is_in_the_interval(lower_limit, upper_limit,user_input) is not True:
       
       
        print("\n Wrong number, please enter a number in the interval: ")


        user_input = int(input("\nPlease enter the number to be guessed by the computer: "))


        #end while

    random_number = produce_random_number_between(lower_limit, upper_limit)


    print("\nEverything is set, lets start the game!!!\n")


    result = now_let_the_computer_guess_the_number(lower_limit, upper_limit, user_input, random_number)

    print(f"CORRECT!!!\nThe number is {result}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    


if __name__ == "__main__":
    main()






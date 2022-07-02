import random 

#rock paper scissors game !!!


# r > s
# s > p
# p > r 


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#GLOBALS

computer_wins = 0
computer_loses = 0
user_wins = 0
user_loses = 0


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#GETTERS

def getUserWins():
    return user_wins

def getUserLoses():
    return user_loses

def getComputerWins():
    return computer_wins

def getComputerLoses():
    return computer_loses


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def userLost():
     print("Sorry you lost, try again next time!!\n")
     global user_loses, computer_wins
     user_loses+=1
     computer_wins+=1

def userWon():
    print("Great!!! You win!!\n")
    global user_wins, computer_loses
    user_wins += 1
    computer_loses+=1


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def show_score():
   
        print("     COMPUTER\n\n\n")
        print(f"W's:  {getComputerWins()}\n\n")
        print(f"L's:  {getComputerLoses()}\n\n\n\n")
        print(f"    USER\n\n\n")
        print(f"W's:     {getUserWins()}\n\n")
        print(f"L's:     {getUserLoses()}\n\n")

      
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def play():

    users_input = input("R for rock, P for paper, S for scissors: ")

    computers_choice = random.choice(['r','p','s'])

    printUsersInput(users_input, computers_choice)

    if users_input == computers_choice:
        print("Tie\n")



    if users_input == 'r' and computers_choice == 'p':
        userLost()
    elif users_input == 'r' and computers_choice == 's':
        userWon()



    elif users_input == 's' and computers_choice == 'r':
       userLost()
    elif users_input == 's' and computers_choice == 'p':
        userWon()
            

    elif users_input == 'p' and computers_choice == 's':
       userLost()
    else:
        userWon()
 #end play()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#printing users and computers choice
def printUsersInput(users_input, computers_choice):

    while isNotValid(users_input):
        print("Sorry invalid input, please type again:\n")
        users_input = input("R for rock, P for paper, S for scissors: ")
        
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #printing users choice in full words
    
    ui = ''
    if users_input == 'p':
        ui = 'paper'
        print(f"So you chose: {ui}")

    elif users_input == 'r':
        ui = 'rock'
        print(f"So you chose: {ui}")

    else:
        ui = 'scissors'
        print(f"So you chose: {ui}")
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #printing computers choice in full words

    cc = ''
    if computers_choice == 'p':
        cc = 'paper'
        print(f"So computer chose: {cc}")

    elif computers_choice == 'r':
        cc = 'rock'
        print(f"So computer chose: {cc}")

    else:
        cc = 'scissors'
        print(f"So computer chose: {cc}")

#end printUsersInput()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#checking if users input is valid
def isNotValid(users_input):
    if users_input == 'r' or users_input == 's' or users_input == 'p':
        return False

    return True


 #end isNotValid()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def print_menu():

    print("   MENU   ")
    print("----------")
    print("1: Play ")
    print("2: Show score ")
    print("3: Exit Program")

 #end print_menu()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#main..
def main():

    print("\nGame of rock paper scissors!! The rules are simple:\n")
    print("Rock beats scissors\n")
    print("Scissors beats paper\n")
    print("Paper beats rock\n")

    print("ok lets play!!\n")

    option = 0
    while option != 3:
        print_menu()
        option = int(input("Type number to choose: \n"))
        if option == 1:
            play()
        elif option == 2:
            show_score()
        else:
            print("\nExiting program, byee..")


 #end main()    
    

if __name__ == "__main__":
    main()



import sys

def collatz(number):
    try:
        while isNotOne(number):
            if isEven(number):
                number = number//2
                print(number)
            else:
                number = 3*number+1
                print(number)

    except KeyboardInterrupt:
        sys.exit

def isNotOne(number):
    return number!=1

    
def isEven(number):
    if number%2 == 0:
        return True
    
    return False

def main():
    collatz(173453)

if __name__ == "__main__":
    main()
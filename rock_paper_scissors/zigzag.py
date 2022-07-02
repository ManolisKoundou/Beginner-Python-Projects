import time, sys

stars = '********'

def zigzag(string, hops):

    try:
        global stars
        blank = ' '
        while True:
            for i in range(1,hops+1):
                print(blank*i+stars+'\n')
                time.sleep(0.1) # Pause for 1/10 of a second.


            for i in range(hops+1,1,-1):
                print(blank*i+stars+'\n')
                time.sleep(0.1) # Pause for 1/10 of a second.


    except KeyboardInterrupt:
        sys.exit()



def main():
    global stars
    zigzag(stars,6)

if __name__ == "__main__":
    main()

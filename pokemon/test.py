class A:

    def __init__(self,number):
        self.number = number

def createA():
    a = A(3)

    return a 

b = createA()
print(b.number)

    
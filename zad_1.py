import random
tab = []
def userInput() -> int: #Function catch wrong input
    while True:
        try:
            return int(input("Hi! Please, enter a nondecimal number"))
        except ValueError:
            print("I'm sorry. Type of input is incorrect. Please, try again.")
def createList(): # Creates list
    a = userInput()
    b = userInput()
    if(b < a):
        for x in range(5):
            tab.append(random.randint(b,a))
            print("Liczba",y+1,":",tab[y])
    if(a < b):
        for y in range(5):
            tab.append(random.randint(a,b))
            print("Liczba",y+1,":",tab[y])
    else:print("It's equal") # Check if input results are equal 
createList()







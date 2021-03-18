"""
Program Goals:
1, Input from user
2, convert to an INT
3, Add to input to a list
4, Pull values from index positions
"""

import random
#create functions that will preform those actions
myList = []

def mainPro():
    while True:
        try:
            print("""
Hello, there! Let's work with lists!""")
            print("Choose one of the following opetions. Type a number only!")
            choice = input("""1, Add to list
2, Mass add random numbers
3, Random choice
4, Linear search
5, Return the value at an index position
6, Print the list
7, End program
    """)
            if choice == "1":
                addList()
            elif choice == "2":
                MassA()
            elif choice == "3":
                ranSer()
            elif choice == "4":
                linear()
            elif choice == "5":
                indexVal()
            elif choice == "6":
                print(myList)
            else:
                break
            
        except:
            print("An error occurred")
            pass

def addList():
    vary = input("please type an integer!     ")
    myList.append(int(vary))
    print (myList)

def MassA():
    print ("We're going to add a bunch of numbers!")
    AddMount = input ("How many should we add?    ")
    AddRang = input ("And how high should the numbers we add be?    ")
    for x in range (0, int(AddMount)):
        myList.append(random.randit(0,int(AddRang)))
    print("Your list is done!")
    
def indexVal():
    inPos = input("What position what would like to pull?     ")
    print (myList[int(inPos)])

def ranSer():
    print("Here is a random value for your list")
    print(myList[random.randint(0, len(myList)-1 )])

def linear():
    print("We're going to saerch throught the list!")
    serchIt = input("What are you looking for? Number-wise?     ")
    for x in range(len(myList)):
        if myList [x] == int(serchIt):
            print("you're item is at index {}".format(x))


if __name__ == "__main__":
    mainPro()


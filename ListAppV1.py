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
searchList = []
speList = []

def mainPro():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following opetions. Type a number only!")
            choice = input("""1, Add to list
2, Mass add random numbers
3, Random choice
4, Linear search
5, Sort List
6, Return the value at an index position
7, Print the list
8, End program
   """)
            if choice == "1":
                addList()
            elif choice == "2":
                massA()
            elif choice == "3":
                ranSer()
            elif choice == "4":
                linear()
            elif choice == "5":
                sortL(myList)
            elif choice == "6":
                indexVal()
            elif choice == "7":
                printL
            else:
                print("Goodbye!")
                break
            
        except:
            print("An error occurred")
            pass

def addList():
    vary = input("please type an integer!    ")
    myList.append(int(vary))
    print (myList)

def massA():
    print ("We're going to add a bunch of numbers!")
    AddMount = input ("How many should we add?    ")
    AddRang = input ("And how high should the numbers we add be?    ")
    for x in range (0, int(AddMount)):
        myList.append(random.randint(0,int(AddRang)))
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
            searchList.append(1)
            print("you're item is at index {}".format(x))
    print("Your number occured {} times.".format(len(searchList)))
    searchList.clear()

def recrusiveBinarySearch(speList, low, high, x):
    if high >= low:
        mid = (high + low)//2
        if speList[mid] == x:
            print ("Oh what luck. Your number is at position {}".format(mid))
        elif speList[mid] > x:
            return recrusiveBinarySearch(speList, low, mid-1, x)
        else:
            return recrusiveBinarySearch(speList, mid+1, high, x)
        
    else:
        print("Your number isn't here!")
          
def sortL(myList):
    for x in myList:
        if x not in speList:
            speList.append(x)
    speList.sort()
    showMe = input("Wanna see the new list?  Y/N    ")
    if showMe.lower() == "y":
        print(speList)

def printL():
    if len(speList) == 0:
        print(myList)
    else:
        which = input ("Sorted or un-sorted")
        if which.lower() == "sorted":
            print(speList)
    
#I want it to tell you how many times the value occured
"""
I could have it add something to a list and then use the amount of things in the list as a variable
Best told the class how to do this but I wanna try my idea to see if it worked.
"""

if __name__ == "__main__":
    mainPro()


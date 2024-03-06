#Imports a Python modual or extention
import random
#Select which class period
periodselect=input("What period? Respond with just the number.")
#Replace class variables with period number
#Represents kids in a  class
P1=["Joseph", "Ezra", "RJ", "Vikram", "Landon", "Ishaan", "Charlie", "Luke H", "Ava", "Peyton", "Luke L", "Bence", "Siya", "Ari Padmanabhan", "Kosta Patel", "Liam Probst", "Cameron Scott", "Rehan Shah", "Emily Shi", "Ahrian Vemuri", "Olivia Yu"]
P2=["hi"]
#Creates a second list so we can remove names from the list and still have the original list intact
P12=P1
P22=P2
#Creates a repeting loop
x=1
 #Creates a random seed(y) by choosing a random number from the range of the class list
if periodselect=="1":
    while x==1:
        print(P12)
        x=0 
        #Closes
        y=random.randint(1, len(P12))
        #Prints the item at that location but need to subtract one because Pythons index starts at 0 not 1
        print(P12[y-1])
        #Checks if you want to remove the item in the list
        Remove=input("Do you want to remove this? Respond with Yes or No")
        if Remove=="Yes":
            #removes it from the list
            P12.remove(P12[y-1])
            print("Removed")
            Roll=input("Do you want to roll again? Respond with Yes or No")
        #if no does nothing
        elif Remove=="No":
            Roll=input("Do you want to roll again? Respond with Yes or No")
        #otherwise says error
        else:
            print("Error")
            input("Press Enter to exit")
        if Roll=="Yes":
            x=1
        elif Roll=="No":
            input("Press Enter to exit")
        else:
            print("Error")
            input("Press Enter to exit")
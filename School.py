#Imports a Python modual or extention
import random
#Select which class period
periodselect=input("What period? Respond with just the number.")
#Replace class variables with period number
#Represents kids in a  class
P1=["Joseph Abebe", "Ezra Adeb", "RJ Bolton", "Vikram Bondada", "Landon Buford", "Ishaan Desai", "Charlie DeVillers", "Luke Hoffman", "Ava Hutchinson", "Peyton Johnson", "Luke Longin", "Bence Montesano", "Siya Narla", "Ari Padmanabhan", "Kosta Patel", "Liam Probst", "Cameron Scott", "Rehan Shah", "Emily Shi", "Ahrian Vemuri", "Olivia Yu"]
P2=["hi"]
#Creates a second list so we can remove names from the list and still have the original list intact
P12=P1
P22=P2
#Creates a repeting loop
x=1
while x==1:
    #Creates a random seed(y) by choosing a random number from the range of the class list
    if periodselect=="1":
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
        #if no does nothing
        elif Remove=="No":
            pass
        #otherwise says error
        else:
            print("Error")
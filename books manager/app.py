from data import database

def main():
    print("----------------******Choose one of the following******------------------")
    print("--------------------1. Press 1 to add a bew book-------------------------")
    print("--------------------2. Press 2 to see all the added books----------------")
    print("--------------------3. Press 3 to read a book----------------------------")
    print("--------------------4. press 4 to delete a book--------------------------")
    print("--------------------5. Press 5 to quit-----------------------------------")
    x= int(input(""))
    if(x==1):
        n=input("Enter the name of the book ")
        a=input("Enter the author of the book ")
        database.add(n,a)
        main()
    if(x==2):
        database.see()
        main()
    if(x==3):
        n=input("Enter the name of the book")
        database.read(n)
        main()
    if(x==4):
        n=(input("enter name of book")).lower
        database.delete(n)
        main()
    if(x==5):
        print("Stopping the program")
    else:
        print("invalid input")
        main()

main()
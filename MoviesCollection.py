
list=[]     
def main():
    print("-------------------------please give input-----------------------------")
    print("---------------Enter 1 to add new movie")
    print("---------------Enter 2 to search for a movie in collecton")
    print("---------------Enter 3 to see your collection")
    print("---------------Enter 4 to quit")
    x = int(input("-----------------your input-----------------------------------"))         
    if(x==1):
        one()
    elif(x==2):
        two()
    elif(x==3):
        print(list)
        main()
    elif(x==4):
        print("stopping program")
    else:
        print("invalid input")
def one():
    name=input("Enter the name of movie")
    director=input("Enter the director")
    year=int(input("enter the release year of movie"))
    list.append({"name":name,"director":director,"year":year})
    main()
def two():
    s= input("enter the name of movie you want to search")
    for n in list:
        if s==n:
            print(f"you do have {n} in your collection")
        else:
            print("you dont have the movie in your collection")
    main()
main()
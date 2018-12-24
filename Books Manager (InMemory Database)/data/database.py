books=[]
def add(name,author):
    books.append({"Name":name,"Author":author,"Read":False})


def see():
    for book in books:
        print(f'Name of the book is {book["Name"]} and its author is {book["Author"]}, Read-{book["Read"]}')

def read(n):
    for name in books:
        if name["Name"]==n:
            name["Read"]=True
        else: print(f"No book with name {n} found in the databse")

def delete(n):
    for name in books:
        if name["Name"]==n:
            books.remove(name)
        else: print(f"No book with name {n} found in the databse")


def add(name,author):
    with open("books.txt","a") as f:
        f.write(f"{name},{author},False" )
        f.write("\n")


def see():
    with open("books.txt","r") as f:
        b=f.readlines()
        for i in b:
            s = i.split(",")
            print(f"The name of book is {s[0].upper()} and the author is {s[1].upper()} and read = {s[2].upper()}")


def read(n):
    l=[]
    with open("books.txt","r") as f:
        z=f.readlines()
        for i in z:
            s=i.split(",")
            if(s[0]==n):
                s[2]="True"
                i = ",".join(s)
                l.append(i)
            else:
                s[2]="False"
                i = ",".join(s)
                l.append(i)
    with open("books.txt","w") as fr:
        fr.write("")
    with open("books.txt","a") as fr:
        for i in l:
            fr.write(i)  
            fr.write("\n")
    

   
        

def delete(n):
    l=[]
    with open("books.txt","r") as f:
        z=f.readlines()
        for i in z:
            s=i.split(",")
            if(s[0]==n):
                pass
            else: l.append(i)
    with open("books.txt","w") as fr:
        fr.write("")
    with open("books.txt","a") as fr:
        for i in l:
            fr.write(i)
 

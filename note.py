import msvcrt
import mysql.connector
#connecting to my database
mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="notes")
print("""Welcome To my note taking program.
Instructions:
You can keep writing your notes even if you press ENTER for a new line.
When you want the program to stop taking note, press "ctrl+S" in a new line.
When asked, enter the name you want to save the note as.""")
print("\nWrite your note:")
notedb= ""
while True:
    notedb+=input()
    c=msvcrt.getch() #getting the key pressed without pressing enter. It returns the byte.
    if ord(c)==19:   #ascii value of ctrl+s
        print("###SAVED###")
        break
    elif (97<=ord(c) and ord(c)<=122) or (65<=ord(c) and ord(c)<=90):  #if its either in (a to z) or(A to Z)
        notedb+= "\n" + chr(ord(c))
        print(chr(ord(c)),end="")
    else:
        notedb+= "\n"
namedb=input("Enter name of note: ")
cursor=mydb.cursor() #adding an sql cursor to execute sql queries
cursor.execute("INSERT INTO mynotes(name,note) VALUES(%s,%s)",(namedb,notedb)) #executing any sql querry
mydb.commit() #always needed to save the last executed query



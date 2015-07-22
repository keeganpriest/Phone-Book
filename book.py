import time
import pickle
import os

PICKLE_FILE = 'book.pickle'

if os.path.exists(PICKLE_FILE):
    open_file = open(PICKLE_FILE, 'rb')
   
    book = pickle.load(open_file)

else:
    book = { 
            "Police": "911"
}
                                

line = ("==========================================================")
print(line)
print("Welcome to 'Phone Book'")
print(line)
print("""Use these commands in curser:                                                                                                              
Add -  adds numbers and users
Edit - edits an existing contact
Search - searches for specific contact, then displays it                                                                                             
Remove - remove users and numbers
Commands - lists all the commands                                                                                                                   
List - display entries in alphabetical order                                                                                                        
Quit - quits program""")
print(line)


while True :
    
    choice = input()
    
    if choice.upper() == "QUIT":
        print(line)
        print("Program Quit")
        print(line)
        break
    
    elif choice.upper() == "COMMANDS":
       print(line)
       print("""Use these commands in curser:                                                                                                       
Add -  adds numbers and users                                                                                                          
Edit - edits an existing contact                                                                                                       
Search - search's for specific contact, then displays                                                                                  
Remove - remove users and numbers                                                                                                      
Commands - lists all the commands                                                                                                     
List - display entries in alphabetical order                                                                                           
Quit - quits program""")
       print(line)

    elif choice.upper() == "ADD":
        
        print(line)
        name = input("Name:").title()
        number = input("Phone Number:")
        book[name] = number
        print(name, "'s information has been added to your book")
        print(line)
    
    
    elif choice.upper() == "REMOVE":
        
        delname = input("Who's number do you want to delete?").title()
        there_ = delname in book
        
        if there_ == False:
            print("That name is not in our data base, sorry!")
        
        if there_ == True:
            book.pop(delname)
            print(delname, "was deleted.")
        
        print(line)
        
    
    elif choice.upper() == "LIST":
        
        print(line)
        
        for x, y in book.items():
            print (x, "-", y)
            
        print(line)
    
    elif choice == "":
        
        print("Look's like you didn't put anything in the curser!")
    
    elif choice.upper() == "SEARCH":
        
        print(line)
        
        while True:
            
        
            srchname = input("Who's number do you want to search? (Enter 'q' to quit search)").title()
        
            if srchname in book.keys() == True:
            
                 print(srchname, "'s number is", book.get(srchname))
            
            elif srchname == "Q":
                
                print("Quitting 'search'")
                break
            
        
            else:
                print(srchname, "not found")
                
            print(line)
                
    elif choice.upper() == "EDIT":
            print(line)
            for x, y in book.items():
                print(x, "-", y)
            del_name1 = input("Who's contact would you like to edit?").title()
            there_1 = del_name1 in book
            if there_1 == False:
                print("That name is not in the phone book")
            if there_1 == True:
                print(line)
                book.pop(del_name1)
                new_name = input("New name:")
                new_number = input("New number:")
                book[new_name] = new_number
                print(line)
        
    else:
        print("Invalid Command")
    
            

print("Saving!")   
save_file = open(PICKLE_FILE, 'wb')
pickle.dump(book, save_file)
save_file.close()        
    
    
    
    

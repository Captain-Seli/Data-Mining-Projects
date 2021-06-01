# """ * Create a Python module with a __main__ , and at least 100 lines of code. You should use 
# if  __name__  ==  "__main__":
# * Define at least 1 class, and at least 1 function for each class you have defined. Your __main__ should instantiate objects of the classes you have designed, and use them to invoke the methods defined in those classes.
# * Use list comprehensions to create lists.
# * Use dictionary comprehensions to create dictionaries.
# * Use at least 1 decision-making statement (if-elif)
# * Use at least 1 looping statement (for or while).
# * Use at least 1 try-except to catch some exceptions.
# * Use the input() function, or command-line arguments, to get some user input
# * Produce some, hopefully interesting, output
# * Add enough comments to make your script easy to understand (not counted toward the 100 line requirement)
# Last but not least, be creative, and make sure it runs before you submit. """ 
# hashlib.sha256(string_to_hash.encode()).hexdigest()

import hashlib

def main():
    if __name__ == __main__:

        class User(self, userName, password):
            userName = self.userName
            password = self.password

        #def makeUser(username, password):
        userName = str(input("Enter Username: \n"))
        password = str(input("Enter Password: \n"))
        hashword = str(haslib.sha256(password.encode().hexdigest())
        print(password)
        print(hasword)

        try:
            userFile = open("userFile.txt")
            userFile.write("This is the user file.")
        except:
            print("Could not write to user file.")
        finally:
            userFile.close()
        main()
    
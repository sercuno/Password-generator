# Importing modules
from random import shuffle, choice
import string

# Storing the characters from string
characters = (string.ascii_lowercase +
              string.ascii_uppercase +
              string.digits +
              string.punctuation)

# The list that will store the characters in the password
storage = list(set())

# Asking the user the amount of digits they want
while True:
    try:
        length = int(input("What's the lenght you want for your password: "))
        if length <= 5:
            print("The password is going to be too small, recommend to use a password more that 5.")
        if length > 25:
             rint("Your password is too long, it would be hard to memorise.")
        if length > 5:
            break
        if length <= 25:
            break
        else:
            print("Enter a positive integer.")
    except ValueError:
        print("Enter a valid integer.")
        
# Generating the password
while len(storage) <= length:
    storage.append(choice(characters))
    
# Shuffling the list that contains the password
shuffle(storage)

# Turning the list into a string variable
password = "".join(storage)

# Printing the password
print(f"Your new password: {password}")

    

# Modules
from random import shuffle, choice

# Values such as symbols, numbers and letter 
lower_letter = "abcdefghijklmnopqrstuvwxyzåøæ"
upper_letter = lower_letter.upper()
symbols = "#$&!/+?*@"
numbers = "1234567890"

# Storing the stuff generated from the iteration
pw = []

# Decide how many digits the user wants for their password
digits = int(input("How many digits do you want for your password?:  "))

# Generates the password
while len(pw) <= digits:
    pw.append(choice(lower_letter))
    pw.append(choice(upper_letter))
    pw.append(choice(symbols))
    pw.append(choice(numbers))

shuffle(pw)
password = "".join(pw)


# Printes the password
print(password)
    
    
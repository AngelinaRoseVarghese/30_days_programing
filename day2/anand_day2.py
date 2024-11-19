'''description:program that generates a random password of a user-specified length'''

while True:
    password = input("Enter a password:")
    if len(password)>=7:
        print("Strong password")
        break
    else:
        print("Weak password")
        print("Try again with another password")

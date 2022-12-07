n=input("Enter a character")
if n.isalpha():
    print("Inputed value is letter")
    if n.isupper():
        print("Letter is upper case")
    elif n.islower():
        print("Letter is lower case")
if n.isdigit():
    print("It is a digit")
    


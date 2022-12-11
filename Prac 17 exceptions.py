while True:
    try:
        input_char=input("enter name")
        if (int(ord(input_char)) >= 48 and
            int(ord(input_char)) <= 57):
            print(" Digit ")
        else:
            print(" Special Character ")
    except:
        print('please enter valid input')

 
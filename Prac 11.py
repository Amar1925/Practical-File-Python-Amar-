def printIndex(str, s):
 
    flag = False
    for i in range(len(str)):
        if (str[i:i + len(s)] == s):
             
            print( i, end =" ")
            flag = True
 
    if (flag == False):
        print("-1")     
str1 = input("Enter string 1")
str2 = input("Enter string 2")
printIndex(str1, str2)

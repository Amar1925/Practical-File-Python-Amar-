num =int(input("Enter number to check prime"))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
def isPrime(n):
  #since 0 and 1 is not prime return false.
  if(n==1 or n==0):
    return False
    
  #Run a loop from 2 to n-1
  for i in range(2,n):
    #if the number is divisible by i, then n is not a prime number.
    if(n%i==0):
      return False
    
  #otherwise, n is prime number.
  return True
  
  
  
# Driver code
N = int(input("Number to generate prime values till n"));
#check for every number from 1 to N
for i in range(1,N+1):
  #check if current number is prime
  if(isPrime(i)):
    print(i,end=" ")
print("Generate first N prime nos")
a = int(input("Enter a number : "))
c = 2
while a!=0:
  for i in range(2,c):
    if c%i==0:
      break
  else:  
    print(c,end=" ")  
    a-=1
  c+=1  

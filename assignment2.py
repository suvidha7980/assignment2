"""
#palindrome
n = 1441
temp = n
rev = 0
while(n>0):
    dig = n%10
    rev = (rev*10) + dig
    n = n//10
if(temp==rev):
    print("this is palindrome no.")
else:
    print("this is not a palindrome no.")"""
########################################################################################################################
"""
#factorial
x = int(input("Insert any number: "))
fact=1
while x > 1:
   fact *= x
   x -= 1
print("The result of factorial = ", fact)"""
########################################################################################################################
"""
# fibbonacci series
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

print("fibbonacci series")
for i in range(1,10):
    print(fib(i),end=" ")"""
########################################################################################################################
"""
# Armstrong number
n = int(input("Enter a number: "))
sum = 0
temp=n
while n > 0:
   dig= n%10
   sum = sum + (dig ** 3)
   n=n//10
if temp == sum:
   print(temp,"is an Armstrong number")
else:
   print(temp,"is not an Armstrong number")"""
########################################################################################################################
"""
#calculator
choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   ans=A+B
elif choice == '-':
   ans=A+B
elif choice == '*':
   ans=A+B
elif choice == '/':
   ans=A+B
else:
   print("Invalid input")

print("the answer is",ans)"""
########################################################################################################################
"""
#patterns
########################################################################################################################
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print(" ")

########################################################################################################################
for i in range(5):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")

########################################################################################################################
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

########################################################################################################################
x=0
for i in range(0,5):
    x+=1
    for j in range(0,i+1):
        print(x,end=" ")
    print(" ")

########################################################################################################################
for i in range(6,0,-1):
    for j in range(0, i - 1):
        print("* ", end="")
    print(" ")"""
########################################################################################################################
"""
#leap year
def CheckLeap(Year):
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year");
  else:
    print ("Given Year is not a leap Year")
Year = int(input("Enter the number: "))
CheckLeap(Year)"""
########################################################################################################################
"""
#prime no.
number = int(input("Enter any number:"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number, "is not prime number")
            break
    else:
            print(number, "is prime number")"""
########################################################################################################################
"""
# find Area in python
PI = 3.14
r = float(input("Enter the radius of a circle:"))
area = PI * r * r
print("Area of a circle = %.2f" %area)"""
########################################################################################################################
"""
#reverse a list
a=[5,"ram",10,"ravi",3]
a.reverse()
print(a)"""
########################################################################################################################
"""
# Program to find the sum of all elements in a list
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
sum = 0
for i in numbers:
    sum = sum + i
print("The sum is", sum)"""
########################################################################################################################
"""
#Average of list elements
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
sum = 0
for i in numbers:
    sum = sum + i
    avg = sum/len(numbers)

print("The average is", avg)"""
########################################################################################################################
"""
#Max of list
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
x = max(numbers)
print(x)"""
########################################################################################################################
"""
#Min of list
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
x = min(numbers)
print(x)"""
########################################################################################################################
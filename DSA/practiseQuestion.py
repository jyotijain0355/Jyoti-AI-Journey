#  1 print hello world?........................................................
print("hello world")
# 2 add two nbumbers?//..........................................................
a=10
b=20
c=a+b
print(c)
# 3 swapppe two numbers?....................................................
a=10
b=20
a,b=b,a
print(a,b)
# 4 square of a numnber........................................................
a = int(input("Enter a number: "))
print(a**2)
# 5 cube of a number..........................................................
a= int (input("Enter a number: "))
print(a**3)
# 6 even or odd..........................................................
a= int(input("Enter your number: "))
if a%2==0:
    print("Even")
else:
    print("Odd")

 ##7 positive or negative olrf zero..............................
a= int(input("Enter your number: "))
if a>0:
    print("Positive")
elif a<0:        
    print("Negative")
else:    print("Zero")        
8# largest of two numbers........................................................
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
if a>b:   
    print("a is greater")    
elif b>a:
    print("b is greater")
else: print("Both are equal")
# 9 largest of three numbers........................................................
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
if a>b and a>c:
    print("a is greater") 
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else: print("All are equal")
#10 check leap year or not........................................................
a= int(input("Enter a year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("Leap year")
else: print("Not a leap year")   
 #sum of n natural numbers........................................................
n= int(input("Enter a number: "))
sum= n*(n+1)//2
print("Sum of n natural numbers is:", sum)
# reverse a number........................................................
a= int(input("Enter a number: "))
reverse=0
while a>0:
    digit= a%10
    reverse= reverse*10 + digit
    a //= 10
print("Reverse of the number is:", reverse)
# palindrome number........................................................
a= int(input("Enter a number: "))
reverse=0
temp=a
while a>0:
    digit= a%10
    reverse= reverse*10 + digit
    a //= 10
if temp==reverse:
    print("Palindrome number")
else: print("Not a palindrome number")
# count digits in a number........................................................
a= int(input("Enter a number: "))
count=0
while a>0:
    a //= 10
    count += 1
print("Number of digits in the number is:", count)   
#sum of digit in a number........................................................
a= int(input("Enter a number: "))
sum=0
while a>0:
    digit= a%10
    sum += digit
    a //= 10    
print("Sum of digits in the number is:", sum)
# product of digits in a number........................................................
a= int(input("Enter a number: "))
product=1
while a>0:
    digit= a%10
    product *= digit
    a //= 10    
print("Product of digits in the number is:", product)     
# amrstrong number........................................................
a= int(input("Enter a number: "))
order= len(str(a))
sum=0
temp=a
while temp>0:
    digit= temp%10
    sum += digit**order
    temp //= 10
if sum==a:
    print("Armstrong number")
else: print("Not an Armstrong number")     
# fibonacii series........................................................
n= int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
if n <= 0:      
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, ":")
    print(a)
else:
    print("Fibonacci sequence up to", n, ":")
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1      
#prime che3ck........................................................
a= int(input("Enter a number: "))
if a>1:
    for i in range(2, int(a**0.5)+1):
        if a%i==0:
            print("Not a prime number")
            break
    else: print("Prime number")
else: print("Not a prime number")               
# # prime numbers in a range........................................................
lower= int(input("Enter lower bound: "))
upper= int(input("Enter upper bound: "))
print("Prime numbers between", lower, "and", upper, ":")
for num in range(lower, upper + 1):
    if num > 1:       
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')       





  

    


















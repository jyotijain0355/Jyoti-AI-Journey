#✅ Q1: User ka naam input lo aur print karo
name = input("Enter your name: ")
print("Hello", name)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

#✅ Q2: Do numbers ka sum
age = int(input("Enter your age: "))
print("After 5 years:", age + 5)
l = float(input("Length: "))
b = float(input("Breadth: "))
c = float(input("Enter Celsius: "))
print("Area =", l * b)#
f = (c * 9/5) + 32

#✅ Q4: Rectangle area
print("Fahrenheit =", f)

#✅ Q6: Basic operations
a = int(input("Enter a: "))

#✅ Q5: Celsius → Fahrenheit
b = int(input("Enter b: "))

print("Add:", a + b)
print("Sub:", a - b)
print("Mul:", a * b)
print("Div:", a / b)
#✅ Q7: Even / Odd
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
#✅ Q8: Positive / Negative / Zero
n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
#✅ Q9: Largest of 2 numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    print("a is greater")
else:
    print("b is greater")
#✅ Q10: Largest of 3 numbers
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")


#✅ Q11: Pass / Fail (marks ≥ 40)
marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
#✅ Q12: Grade System
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
#✅ Q13: Leap Year Check
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
#✅ Q14: Vowel / Consonant
ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
#✅ Q15: Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
#✅ Q16: 1 se 100 tak print
for i in range(1, 101):
    print(i)
#✅ Q17: Even numbers print (1–100)
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
#✅ Q18: Table print (user input)
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
#✅ Q19: Factorial
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
#✅ Q20: Reverse Number
n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)

#✅ Q21: String reverse karo
s = input("Enter string: ")
print(s[::-1])

#👉 Trick: slicing [::-1]

#✅ Q22: Palindrome check
s = input("Enter string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#✅ Q23: Vowels count karo
s = input("Enter string: ")
count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels =", count)
#✅ Q24: Words count karo
s = input("Enter sentence: ")
words = s.split()
print("Words =", len(words))
#✅ Q25: Uppercase → Lowercase
s = input("Enter string: ")
print(s.lower())

#✅ Q26: List ka sum
lst = [1, 2, 3, 4, 5]
print("Sum =", sum(lst))
#✅ Q27: Largest element
lst = [10, 25, 5, 40, 15]
print("Max =", max(lst))
#✅ Q28: Duplicate remove karo
lst = [1, 2, 2, 3, 4, 4]
unique = list(set(lst))
print(unique)
#✅ Q29: List reverse karo
lst = [1, 2, 3, 4]
print(lst[::-1])
#✅ Q30: Second largest element
lst = [10, 20, 5, 40, 30]

lst = list(set(lst))   # duplicates remove
lst.sort()

print("Second Largest =", lst[-2])


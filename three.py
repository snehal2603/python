# a='nature'
# for char in a:
#     print(char)
# Accept an integer and Print hello world n times
n=int(input('expected outpuut no : '))
for i in range(n):
    print(f'{i+1}. hello')


# - Print natural number up to n
n=int(input('give n : '))
for i in range(n):
    print(i+1)
# - Reverse for loop. Print n to 1
n=int(input('num dedo na : '))
for i in range(n,0,-1):
    print(i)
# - Take a number as input and print its table
n=int(input("print the  num : "))
for i in range(1,11,1):
    print(f"{n}*{i}={n*i}")
# - Sum up to n terms
n=int(input('n terms:'))
sum=0
for i in range(1,(n+1),1):
    sum+=i
print(sum)
# - Factorial of a number
fact=1
n=int(input("num "))
for i in range(1,n+1,1):
    fact*=i
print(fact)    
# - Print the sum of all even & odd numbers in a range
# separately
evensum = 0
oddsum = 0

n = int(input("Enter number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        evensum += i
    else:
        oddsum += i

print(f"Even sum is {evensum} and Odd sum is {oddsum}")           
# - Print all the factors of a number
n=int(input('enter the num'))
for i in range(1,n+1,1):
    if(n%i==0):
        print(i)
# - Accept a number and check if it a perfect number or not.
#  A number whose sum of factors is equal to the number itself
#  Ex - 6 = 1, 2, 3 =6
n=int(input("enter the number : "))
sum=0
for i in range(1,n,1):
    if(n%i==0):
        sum+=i
        if(sum==n):
            print("perfect number.")  

print("not a perfect number .")          


# - Check wether the number is prime or not
n = int(input("number: "))

if n <= 1:
    print("not a prime no")
else:
    for i in range(2, n):
        if n % i == 0:
            print("not a prime no")
            break
    else:
        print("prime no")
        
# - Reverse a string without using in build functions.4
a=input("enter a string : ")
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
# - Check string is Pallindrome or not
a=input("enter a string : ")
rev=""
for i in range(len(a)-1,-1,-1):
    rev+=a[i]
if(a==rev):
    print("palindrome")
else:
    print("not a palindrome")    
 
# - Count all letters, digits, and special symbols from a given
# string


#  Given: str1 = "P@#yn26at^&i5ve"

#  Expected Outcome:

#  Total counts of chars, digits, and symbols

#  Chars = 8

#  Digits = 3

#  Symbol=4    
a = input("Enter a string: ")

charcount = 0
digitscount = 0
symbolcount = 0

for i in a:
    if ('A' <= i <= 'Z') or ('a' <= i <= 'z'):
        charcount += 1
    elif '0' <= i <= '9':
        digitscount += 1
    else:
        symbolcount += 1

print("Chars =", charcount)
print("Digits =", digitscount)
print("Symbol =", symbolcount)
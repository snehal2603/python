# answer True and False

# print(126 > 130)

# print((456 == 456) != (235 == 236))

# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)

# print(True and bool(0))

# Q1. Accept two numbers and print the greatest between them.
# a=int(input('num 1 : '))
# b=int(input("num 2: "))
# if a>b:
#     print(f'{a} is the greatest no rather than {b}')
# else:
#     print(f"{b} is greater than {a}")    

# Q2. Accept the gender from the user as char and print the respective greeting message#  Ex - Good Morning Sir (on the basis of gender)

# a=input('enter the name  : ')
# b=input('enter the male and female  as m/f: ')
# if b=='m':
#     print(f'Good Morning {a} Sir')
# else:
#     print(f'Good Morning {a} Mam')

# Q3. Accept an integer and check whether it is an even number or odd.
'''a=int(input('num 1 '))
if(a%2==0):
    print(f"{a} is even number ")
else:
    print(f'{a} is odd number ')    
'''
# # Q4. Accept name and age from the user. Check if the user is a  valid voter or not.
# a=input('enter the name : ')
# age=int(input("enter the age : "))
# if(age>=18):
#     print(f'{a} is valid voter and age is { age}')
# else:
#     print(f'{a} is not the valid voter and age is {age}') 
#     print(f'{a} will be valid voter after {18-age} years')   

#  Ex- “hello shery you are a valid voter”

# Q5. Accept a year and check if it a leap year or not (google to 

#  find out what is a leap year
# year=int(input('enter the year'))
# if(year%100==0 and year%400==0):
#     print(f'this {year} is century leap year')
# elif (year%4==0):
#     print(f'this {year} is leap year')
# else:
#     print(f"this{ year} is not an leap year")

# take the input of temperature in celsiusX
# @ Below 0°C → "Freezing Cold b
# @ 0°C to 10°C → "Very Cold b
# @ 10°C to 20°C → "Cold b
# @ 20°C to 30°C → "Pleasant b
# @ 30°C to 40°C → "Hot b
# @ Above 40°C → "Very Hot " 
temp=int(input('enter temp in deg celcius : '))
if(temp<0):
    print("freezing cold")
elif(temp<10):
    print('very cold')
elif(temp<20):
    print('cold')  
elif(temp<30):
    print('pleasent')
elif(temp<40):
    print('hot')    
else:
    print('humid')             

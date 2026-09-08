#exception handling 
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Division =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")
#file handling :-
r=open("funstuff.txt",'a')
r.write("this is the funstuff file .. you can do whatever you want . u ccan just say a word or a sent.")
r.close()
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
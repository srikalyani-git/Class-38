num = float(input("Enter a number: "))
if num > 50:
    if num % 2 == 0:
        print("The number is greater than 50 and even")
    else:
        print("The number is greater than 50 and odd")
else:
    print("The number is less")
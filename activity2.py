num = int(input("Enter a number: "))

if num % 3 == 0:
    print("buzz ")
elif num % 5 == 0:
    print("fizz ")
elif num % 15 == 0:
    pass
elif num % 20 == 0:
    print("twist ")
else:
    print(num)
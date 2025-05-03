a = input("Enter a word in capital: ")

letter = input("Enter a capital letter: ")

for i in a:
    if i == letter:
        print(f"{letter} is in {a}")
        break
    
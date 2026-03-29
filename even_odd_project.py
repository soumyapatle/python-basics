print("=== Even Odd Checker Project ===")

while True:
    num = int(input("\nEnter a number: "))

    if num % 2 == 0:
        print(num, "is an Even number")
    else:
        print(num, "is an Odd number")

    choice = input("Do you want to check another number? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using the program!")
        break

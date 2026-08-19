def calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = num1 + num2
            print(f"Result: {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"Result: {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"Result: {result}")

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"Result: {result}")

        elif choice == "5":
            if num2 == 0:
                print("Error: Cannot calculate modulus by zero.")
            else:
                result = num1 % num2
                print(f"Result: {result}")

        else:
            print("Invalid operation.")

    except ValueError:
        print("Invalid input. Please enter numbers.")


while True:
    calculator()

    again = input("\nDo you want to perform another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break

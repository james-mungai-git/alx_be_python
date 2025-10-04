def safe_divide():
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))

        result = numerator / denominator

    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result is: {result}")


# Run the function
safe_divide()

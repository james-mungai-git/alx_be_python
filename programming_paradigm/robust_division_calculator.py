def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Both inputs must be numbers."
    finally:
        print("Division attempt complete.")

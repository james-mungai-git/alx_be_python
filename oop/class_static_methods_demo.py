class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers and reference a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(5, 7)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(5, 7)
    print(f"Product: {product_result}")

# multiplication_table.py

# Ask user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate multiplication table up to 10
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

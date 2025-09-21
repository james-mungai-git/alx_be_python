# multiplication_table.py

# Ask user for a number
num = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

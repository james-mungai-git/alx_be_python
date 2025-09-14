monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = int(monthly_income - monthly_expenses)

print(f"Your monthly savings are $ {monthly_savings}")

# Define interest rate
interest_rate = 0.05

# Calculate projected savings after one year
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Print result
print(f"Projected savings after one year, with interest, is: {projected_savings}")

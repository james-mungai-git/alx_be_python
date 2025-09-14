# finance_calculator.py

# Define variables
monthly_income = 3000
monthly_expenses = 2000

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Define interest rate
interest_rate = 0.05

# Calculate projected savings after one year
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Print result
print(f"Projected savings after one year, with interest, is: {projected_savings}")

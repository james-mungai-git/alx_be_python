monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = int(monthly_income - monthly_expenses)

print(f"Your monthly savings are $ {monthly_savings}")

interest_rate = 0.05

Projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

print(f"Projected savings after one year, with interest, is: {Projected_savings}")

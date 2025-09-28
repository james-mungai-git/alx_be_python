from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(" Current Date and Time:", formatted_date)
    return current_date  # return so we can use it in Part 2

# Part 2: Calculate Future Date
def calculate_future_date(current_date):
    days_to_add = int(input("Enter number of days to add: "))
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(" Future Date:", formatted_future_date)

# Main Program
def main():
    today = display_current_datetime()
    calculate_future_date(today)

# Run the program
if __name__ == "__main__":
    main()

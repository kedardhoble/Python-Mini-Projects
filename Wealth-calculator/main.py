import sys
import matplotlib.pyplot as plt

# Function to calculate wealth by year and return a list of results
def calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years):
    total_savings = current_wealth
    wealth_by_year = []  # List to store the total wealth at the end of each year
    for year in range(1, years + 1):
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)
        wealth_by_year.append(total_savings)  # Store the wealth for this year
    return wealth_by_year

# Function to calculate years until a target wealth is reached
def calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth):
    total_savings = current_wealth
    years_to_freedom = 0
    while True:
        years_to_freedom += 1
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)
        if total_savings > target_wealth:
            return years_to_freedom

# Main function to interact with the user
def main():
    prog = input("Which program would you like to run? Type 'returns' or 'freedom': ")
    try:
        current_wealth = float(input("Enter your current wealth: "))
        rate_of_return = float(input("Enter estimated rate of return (%): "))
        monthly_savings = float(input("Enter how much you can save per month: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        sys.exit()

    if prog == 'returns':
        years = int(input("Enter investment period in years: "))
        wealth_by_year = calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years)

        # Create a list of years for the x-axis
        years_list = list(range(1, years + 1))

        # Plot the data for returns.
        plt.plot(years_list, wealth_by_year, marker='o', linestyle='-', color='b', label='Total Wealth')
        plt.xlabel('Years')
        plt.ylabel('Total Wealth ($)')
        plt.title('Wealth Growth Over Time')
        plt.grid(True)
        plt.legend()
        plt.show()

    elif prog == 'freedom':
        try:
            target_wealth = float(input("How much money do you need to be financially free? "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            sys.exit()
        years_to_freedom = calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth)
        print(f"You will reach financial freedom in {years_to_freedom} years! Keep going!")
        
    else:
        print("Invalid input. Please type 'returns' or 'freedom'.")
        
main()

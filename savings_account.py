"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(self, balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Prompt the user to enter the information for each parameter.
    balance = float(input("Enter the balance of the savings account: "))
    interest_rate = float(input("Enter the interest rate of the savings account: "))
    months = int(input("Enter the number of months of the investment: "))
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    # Hint: You need to add the interest as a value, i.e, 0.

    savings = Account(balance, interest_rate)
    
    # Calculate interest earned
    interest_earned = float(balance * (SavingsAccount.set_interest()/100 * SavingsAccount.get_months()/12)) 
    print(f"Your interest earned is : {interest_earned} ")

    # Calculate new balance
    balance += interest_earned
    """Creating a savings Account class with methods"""

    # Call the parent class's __init__ method and pass the required arguments
    Account.__init__(self, balance, interest_rate)

    return self.interest_earned
    return self.balance

    # # This method gets the length of months for the CD.
    # def get_months(self):
    #     """Gets the length of the investment"""
    #     return self.months




    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE

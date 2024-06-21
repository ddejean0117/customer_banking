"""Import the Account class from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
 
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    savings = Account(balance, interest_rate)
    
    # Set earned interest to 0
    savings.set_interest(0)

    # Calculate interest earned
    interest_earned = round(float(balance * (interest_rate/100 * months/12)),2)
    
    # Calculate new balance
    balance += interest_earned

    # Use the setter methods to change the information
    savings.set_balance(balance)
    savings.set_interest(interest_earned)

    # Return interest earned and balance values
    return balance, interest_earned
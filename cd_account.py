"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account


def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    CD = Account(balance, interest_rate)
    
    # Set earned interest to 0
    #CD.set_interest(0)

    # Calculate interest earned
    interest_earned = round(float(balance * (interest_rate/100 * months/12)),2)

    # Calculate new balance
    balance += interest_earned

    # Use the setter methods to change the information
    CD.set_balance(balance)
    CD.set_interest(interest_earned)

    # print savings instance
    # print(CD.balance) 
    # print(CD.interest)

    # Return interest earned and balance values in a tuple
    return balance, interest_earned

# Prompt the user to enter the information for each parameter.
# balance = float(input("Enter the balance of the CD account: "))
# interest_rate = float(input("Enter the interest rate of the CD account: "))
# months = int(input("Enter the number of months of the CD investment: "))

balance = 0
interest_rate = 0
months = 0

# Capture the return result of the create_savings_account function in a tuple
#CDresult = create_cd_account(balance, interest_rate, months)

# print(f"Your interest earned is: ${CDresult[1]} ")
# print(f"Your new balance with interest is: ${CDresult[0]} ")



    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

    # Calculate interest earned
    # ADD YOUR CODE HERE

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE

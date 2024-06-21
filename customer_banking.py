# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the balance of the savings account: "))
    savings_interest = float(input("Enter the interest rate of the savings account: "))
    savings_maturity = int(input("Enter the number of months of the savings investment: "))
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, sav_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your savings interest earned is: ${updated_savings_balance} ")
    print(f"Your new savings balance with interest is: $ {sav_interest_earned} ")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the balance of the CD account: "))
    cd_interest = float(input("Enter the interest rate of the CD account: "))
    cd_maturity = int(input("Enter the number of months of the CD investment: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your CD interest earned is: ${updated_cd_balance} ")
    print(f"Your new CD balance with interest is: $ {cd_interest_earned} ")

if __name__ == "__main__":
    # Call the main function.
    main()
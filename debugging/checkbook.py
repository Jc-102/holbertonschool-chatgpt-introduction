#!/usr/bin/python3
"""
A simple command-line checkbook that lets the user deposit money,
withdraw money, and check their balance.
"""


class Checkbook:
    """
    Represents a checkbook that tracks a single account balance.

    Attributes:
        balance (float): The current account balance, starting at 0.0.
    """

    def __init__(self):
        """
        Function Description:
            Initializes a new Checkbook with a balance of 0.0.

        Parameters:
            None

        Returns:
            None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds a positive amount to the balance and prints the
            deposited amount and the new balance.

        Parameters:
            amount (float): The amount of money to deposit.
                            Must be greater than 0.

        Returns:
            None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Subtracts a positive amount from the balance if there are
            sufficient funds, then prints the withdrawn amount and the
            new balance. Prints an error message otherwise.

        Parameters:
            amount (float): The amount of money to withdraw.
                            Must be greater than 0 and not exceed
                            the current balance.

        Returns:
            None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
            Prints the current balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_amount(prompt):
    """
    Function Description:
        Prompts the user for a monetary amount and converts it to a
        float. Prints an error message if the input is not numeric.

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        float: The amount entered by the user, or None if the input
               was not a valid number.
    """
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None


def main():
    """
    Function Description:
        Runs the interactive checkbook loop. Repeatedly asks the user
        for a command (deposit, withdraw, balance, exit) and performs
        the matching action until the user types 'exit'.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = get_amount("Enter the amount to deposit: $")
            if amount is not None:
                cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = get_amount("Enter the amount to withdraw: $")
            if amount is not None:
                cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
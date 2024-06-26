from random import randint

account_balance = 0
is_running = True
account_name = None
account_id = randint(10000, 99999)

def create_account():
    global account_name, account_id
    account_name = input("Enter your name: ")
    print(f"Account created successfully! {account_name}'s account ID is: {account_id}")

def delete_account():
    global account_id
    print(f"Account with ID {account_id} has been deleted successfully")
    account_id = None

def show_balance():
    global account_balance
    print(f"Your current balance is P{account_balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    
    if amount < 0:
        print("Invalid amount. Please enter a positive value.")
    else:
        return amount

def withdraw():
    global account_balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount < 0:
        print("Invalid amount. Please enter a positive value.")
    elif amount > account_balance:
        print("Insufficient balance")
    else:
        return amount

while is_running:
    print("\nMy Bank System")
    print(f"Hello, {account_name}!")
    print("a. Create Account")
    print("b. Show Balance")
    print("c. Deposit")
    print("d. Withdraw")
    print("e. Delete Account")
    print("f. Exit")

    choice = input("Enter your choice (a-f): ")
    
    if choice == 'a':
        create_account()
    elif choice == 'b':
        show_balance()
    elif choice == 'c':
        deposit_amount = deposit()
        if deposit_amount:
            account_balance += deposit_amount
    elif choice == 'd':
        withdraw_amount = withdraw()
        if withdraw_amount:
            account_balance -= withdraw_amount
    elif choice == 'e':
        delete_account()
    elif choice == 'f':
        break
    else:
        print("Invalid choice. Please select a valid option.")
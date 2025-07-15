                    # MİNİ BANK PROJECT FOR PYTHON BEGİNNERS ^^

# 1: Get name and balance information from user
name = input("Your name: ")
balance = float(input("Enter your starting balance: "))
print(f"Hello {name}, your starting balance is {balance} Dollar.")

# 2: Action Menu
while True:
    print("\n1 - Deposit Money")
    print("2 - Withdrawal")
    print("3 - Balance Inquiry")
    print("4 - Exit")

    choose = input("Select the action you want to perform (1-4): ")

    if choose == "1":
        # Deposit process
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount} TL deposited. Your total balance is now {balance} Dollar.")
        else:
            print("Please enter a valid amount.")

    elif choose == "2":
        # Withdrawal process
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Sorry, your balance is not enough.")
        elif amount <= 0:
            print("Please enter a valid amount.")
        else:
            balance -= amount
            print(f"{amount} TL withdrawn. Your current balance is {balance} Dollar.")

    elif choose == "3":
        # Balance inquiry
        print(f"Your current balance is {balance} Dollar.")

    elif choose == "4":
        print("Exiting... Have a nice day!")
        break

    else:
        print("Invalid selection. Please choose between 1 and 4.")

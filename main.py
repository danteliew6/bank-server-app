from Controller import Controller
business_controller = Controller()
customer = business_controller.login()
if customer:
    options = {
        1: business_controller.show_balance,
        2: business_controller.withdraw_money,
        3: business_controller.deposit_money,
        4: business_controller.transfer_funds,
        5: business_controller.display_last_transactions,
        6: business_controller.logout
    }

    while True:
        print("\nActions:")
        print("1. Show Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Funds")
        print("5. Display Last 10 Transactions")
        print("6. Log out")

        choice = int(input("Enter your choice (1-6): "))

        if choice in options:
            if choice >= 6:
                options[choice]()
            else:
                options[choice](customer)
        else:
            print("Invalid choice. Please try again.")

        if choice == 6:
            break
else:
    print("Login failed.")
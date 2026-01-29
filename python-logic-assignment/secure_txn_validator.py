balance=float(input("Enter your account balance: "))
withdrawal_amount=float(input("Enter the withdrawal amount: "))
verify_status=input("Is your account verified? (yes/no): ").strip().lower()
is_verified=verify_status=="yes"

if balance>=withdrawal_amount and is_verified:
    print("Withdrawal successful")
    print(f"New balance: {balance - withdrawal_amount}")
else:
    print("Transaction denied")
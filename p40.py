balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))
minimum_balance = float(input("Enter minimum balance required: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount")

elif withdrawal > balance:
    print("Withdrawal rejected: Insufficient balance")

elif balance - withdrawal < minimum_balance:
    print("Withdrawal rejected: Minimum balance must be maintained")

else:
    balance = balance - withdrawal
    print("Withdrawal approved")
    print("Remaining balance =", balance)

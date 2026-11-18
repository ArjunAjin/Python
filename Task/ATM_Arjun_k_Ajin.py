# Store the initial balance and withdrawal amount in variables. 
# initial_balance=5000
# withdrawl = 1350
Balance = 5000
withdrawal = 1350

# Calculate the remaining balance. 
remaining_balance = Balance - withdrawal
print('Remaining_Balance',remaining_balance)

# Check whether the withdrawal amount is less than the available balance
print('withdrawal amount is < available balance', withdrawal < Balance)

# Check whether the remaining balance is greater than ₹1,000. 
print('remaining balance >= 1000',remaining_balance > 1000)

# Calculate how many ₹500 notes and how much remainder will be needed to  represent the remaining balance. 
note= remaining_balance//500
remainder = remaining_balance % 500
print('500 rupee notes',note)
print('Remainderc', remainder)








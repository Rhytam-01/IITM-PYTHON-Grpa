def process_transactions(n, initial_balance, transactions):
    balances = []
    current_balance = initial_balance
    
    for day in range(n):
        daily_transactions = transactions[day]
        min_balance = current_balance
        max_balance = current_balance
        
        for transaction in daily_transactions:
            current_balance += transaction
            min_balance = min(min_balance, current_balance)
            max_balance = max(max_balance, current_balance)
        
        balances.append((min_balance, max_balance, current_balance))
    
    return balances

# Reading input
n = int(input())
initial_balance = int(input())
transactions = []

for _ in range(n):
    daily_transactions = list(map(int, input().split()))
    transactions.append(daily_transactions)

# Processing transactions
results = process_transactions(n, initial_balance, transactions)

# Printing results
for result in results:
    print(f"{result[0]},{result[1]},{result[2]}")

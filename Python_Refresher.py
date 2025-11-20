#This is python refresher problem solving sessions

#Problem 1 – Smart Expense Tracker (Control Flow + Collections)

transactions = [
    {"type": "food", "amount": "12.50"},
    {"type": "rent", "amount": "800"},
    {"type": "entertainment", "amount": "25.99"},
    {"type": "food", "amount": "abc"},       # invalid
    {"type": "other", "amount": "-5"},       # suspicious
]

total_spent = 0     #sum of all value
total_per_type = {} #create dictionary to filter and add total
suspicious_entries = []

for item in transactions:
    
    try:            #check if invalid value
        amount = float(item["amount"])
    except ValueError:
        continue

    if amount <=0:  #add to suspicious items list if negative or 0
        suspicious_entries.append(item)

    total_spent += amount   #sum it
    category = item["type"]
    if category in total_per_type:
        total_per_type[category]+= amount
    else:
        total_per_type[category] = amount

print("-"*30)
print(f"List of suspicious entries: {suspicious_entries}")
print(f"Totals per type: {total_per_type}")
print(f"Overall Total Spent: {total_spent}")

def process_transactions(my_data):
    total_spent = 0     #sum of all value
    total_per_type = {} #create dictionary to filter and add total
    suspicious_entries = []

    for item in transactions:
        
        try:            #check if invalid value
            amount = float(item["amount"])
        except ValueError:
            continue

        if amount <=0:  #add to suspicious items list if negative or 0
            suspicious_entries.append(item)

        total_spent += amount   #sum it
        category = item["type"]
        if category in total_per_type:
            total_per_type[category]+= amount
        else:
            total_per_type[category] = amount

    print("-"*30)
    print(f"List of suspicious entries: {suspicious_entries}")
    print(f"Totals per type: {total_per_type}")
    print(f"Overall Total Spent: {total_spent}")

process_transactions(transactions)
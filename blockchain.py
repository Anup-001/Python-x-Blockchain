#initialize blockchain list
blockchain= []

def get_last_blockchain_value():
    """returns the last value of the current blockchain"""
    return blockchain[-1]

def add_value(transaction_amount,last_transaction=[1]):
    """append a new value as well as the last blockchain value"""
    blockchain.append([last_transaction,transaction_amount])

def  get_user_input():
    return float(input("Enter transaction amount: $"))
    
tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(tx_amount,get_last_blockchain_value())
tx_amount = get_user_input()
add_value(tx_amount,get_last_blockchain_value())

print(blockchain)
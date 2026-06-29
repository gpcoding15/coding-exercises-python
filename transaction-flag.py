# Ejercicios recomendados para practicar
# 1. Flag de transacciones por monto alto

# Dado un listado de transacciones:

# transactions = [
#     {"id": "t1", "user_id": "u1", "amount": 120},
#     {"id": "t2", "user_id": "u2", "amount": 5000},
# ]

# Devolvé los IDs de las transacciones cuyo amount > threshold.

# Antes de codearlo, pensá:

# ¿Qué estructura de datos necesitás realmente?
# ¿Cuál es la complejidad temporal?
# ¿Qué pasa si el monto viene como string, negativo o None?

def get_transactions_higher_than_threshold(transactions, threshold):
    flagged_transactions = []

    if not isinstance(threshold(int, float)):
        raise ValueError("threshold should be a number")
    
    for transaction in transactions:
        amount = transaction.get("amount")
        transaction_id = transaction.get("id")

        if not isinstance(amount, int, float):
            raise ValueError("amount should be a number")
        
        if amount > threshold :
            flagged_transactions.append(transaction_id)

    return flagged_transactions
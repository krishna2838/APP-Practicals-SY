import sys

# Base Strategy Class
class TransactionHandler:
    def process_payment(self, bill_amount):
        pass

# Concrete Strategy 1
class CardTransaction(TransactionHandler):
    def process_payment(self, bill_amount):
        print(f"Successfully paid ₹{bill_amount} via Credit/Debit Card.")

# Concrete Strategy 2
class UPITransaction(TransactionHandler):
    def process_payment(self, bill_amount):
        print(f"Successfully paid ₹{bill_amount} via UPI (GPay).")

# Context Class
class TransactionManager:
    def __init__(self, handler):
        self.current_handler = handler

    def change_handler(self, new_handler):
        self.current_handler = new_handler

    def execute(self, bill_amount):
        self.current_handler.process_payment(bill_amount)


# --- Automated Testing Section ---
card_processor = CardTransaction()
manager = TransactionManager(card_processor)
manager.execute(1000)

gpay_processor = UPITransaction()
manager.change_handler(gpay_processor)
manager.execute(500)


# --- Interactive CLI Section ---
print("\n====== Checkout Gateway ======")
try:
    total_amount = float(input("Please enter the bill amount: ₹"))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    sys.exit()

print("\nAvailable Payment Methods:")
print("1 -> Card Payment")
print("2 -> Google Pay (UPI)")

user_option = int(input("Select your preferred option (1/2): "))

if user_option == 1:
    selected_strategy = CardTransaction()
elif user_option == 2:
    selected_strategy = UPITransaction()
else:
    print("Transaction Failed: Invalid selection.")
    sys.exit()

# Execute final transaction
final_checkout = TransactionManager(selected_strategy)
final_checkout.execute(total_amount)
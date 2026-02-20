# Case Study-1: Grocery Store Billing System
# Subject: AI102P
# This program calculates the total cost of 3 items
# and applies a 10% discount if total exceeds $50

# Taking input for 3 items
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Calculating total cost
total = item1 + item2 + item3

# Initialize discount
discount = 0.0

# Apply 10% discount if total is greater than $50
if total > 50:
    discount = total * 0.10

# Calculate final payable amount
final_amount = total - discount

# Display results
print("\n----- BILL SUMMARY -----")
print(f"Original Total: ${total:.2f}")
print(f"Discount Applied: ${discount:.2f}")
print(f"Final Payable Amount: ${final_amount:.2f}")
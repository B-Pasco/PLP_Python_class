"""
PROMPT:
1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
"""

def calculate_discount(price_of_item, discount):
    if discount_percent >= 20:
        final_price = price - (price_of_item * discount / 100)
        return final_price
    elif discount < 20:
        return price

# Taking user input.
price = float(input("Enter the price of item: "))
discount_percent = float(input("Enter the discount percentage btn 1 and 100: "))

# Calling function to calculate the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price after applying the discount is {final_price}")


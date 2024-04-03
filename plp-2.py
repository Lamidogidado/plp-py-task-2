def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
      price: The original price of the item.
      discount_percent: The discount percentage (0 to 100).

  Returns:
      The final price after applying the discount, or the original price
      if the discount is less than 20%.
  """
 
  discount = discount_percent /100
  if discount >= 0.2:
    return price * (1 - discount)
  else:
    return price 
  
  # Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0 to 100): "))

# Calculate and display final price
final_price = calculate_discount(original_price, discount_percent)
print(f"Final price after applying {discount_percent}% discount: ${final_price:.2f}")



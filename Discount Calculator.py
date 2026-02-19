price = float(input("Enter the product price: "))
discont = float(input("Enter the discount percentage: "))
new_price = price - (price * discont/100)
print(f"The new price is, {new_price:.2f}")
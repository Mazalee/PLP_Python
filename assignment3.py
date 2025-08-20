def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        return price - discount_amount
    else: 
        return price
    
price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percentage)

print("The final price after discount:", final_price)
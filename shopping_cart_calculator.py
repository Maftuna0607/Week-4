print("SHOPPING CART CALCULATOR")
print("========================================")
def calculate_item_total(quantity, unit_price):
    return quantity*unit_price
    
def apply_bulk_discount(total, quantity):
    if quantity >=10:
        return(total*10)/100
    elif quantity>=5:
        return(total*5)/100
    else:
        return 0

def calculate_tax(subtotal, tax_rate):
    return subtotal* (tax_rate/100)

def is_eligible_for_free_shipping(subtotal):
    return subtotal >=50
    
def process_order(item_name, quantity, unit_price, tax_rate):
    item_total=calculate_item_total(quantity,unit_price)
    discount=apply_bulk_discount(item_total,quantity)
    subtotal=item_total-discount
    tax=calculate_tax(subtotal,tax_rate)
    free_shiping_eligible=is_eligible_for_free_shipping(subtotal)
    final_total=subtotal+tax

    print(f"Order Reciept for: {item_name}")
    print(f"Quantity: {quantity}, {unit_price:.2f} each")
    print(f"Item Total: ${item_total:.2f}")
    print(f"Bulk Discount: -${discount:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax ({tax_rate}%): {tax:.2f}")
    print(f"Final Total: ${final_total:.2f} ")
    if free_shiping_eligible:
        print("Your order will be shiped for free")
    else:
        shiping_cost=50-subtotal
        print(f"Need ${shiping_cost:.2f} more for free shiping")
    print("----------------------------------------")

process_order("Notebook",12,3.5,8)
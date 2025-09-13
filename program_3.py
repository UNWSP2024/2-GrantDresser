def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    item1 = float(input("Enter price of item 1:10.99 "))
    item2 = float(input("Enter price of item 2:3.49 "))
    item3 = float(input("Enter price of item 3:7.25 "))
    item4 = float(input("Enter price of item 4:29.99 "))
    item5 = float(input("Enter price of item 5:15.99 "))

    # Calculate subtotal
    subtotal = item1 + item2 + item3 + item4 + item5

    # Calculate sales tax
    sales_tax = subtotal * 0.07

    # Calculate total
    total = subtotal + sales_tax

    # Display the results
    print("Subtotal: $", subtotal)
    print("Sales Tax: $", sales_tax)
    print("Total: $", total)



calculate_total_purchase()
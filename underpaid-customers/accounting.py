def over_or_underpaid(file_name):
   
   the_file = open(file_name)
   for line in the_file:
        line = line.rstrip()
        tokens = line.split('|')

        customer_name = tokens[1]
        quantity_ordered = float(tokens[2])
        amount_paid = float(tokens[3])

        if quantity_ordered != amount_paid:
            print(f"{customer_name} paid ${amount_paid:.2f},", f"expected ${quantity_ordered:.2f}")

over_or_underpaid("customer-orders.txt")

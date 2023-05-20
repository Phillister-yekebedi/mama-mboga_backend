
class Order:
    def __init__(self, order_number, customer_name, total_price):
        self.order_number = order_number
        self.customer_name = customer_name
        self.total_price = total_price
        self.is_paid = False

    def process_payment(self, payment_gateway, phone_number, pin):
        self.payment_gateway = payment_gateway
        self.phone_number = phone_number
        self.pin = pin
        if not self.is_paid:
            success = payment_gateway.process_payment(self.total_price, phone_number, pin)
            if success:
                self.is_paid = True
                return True
            else:
                return False
        else:
            print("Order has already been paid.")
            return False
        
        
order1 = Order(1, "John Doe", 100.0)
print("Order Number:", order1.order_number)
print("Customer Name:", order1.customer_name)
print("Total Price:", order1.total_price)
print("Is Paid:", order1.is_paid)
            

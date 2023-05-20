

class Payment:
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
                return True, "Payment processed successfully.."
            else:
                return False, "Payment processing failed."
        else:
            return False, "Order has already been paid."
        
        
order1 = Payment(1, "Yvonne Atieno", 200.0)
print("Order Number:", order1.order_number)
print("Customer Name:", order1.customer_name)
print("Total Price:", order1.total_price)
print("Is Paid:", order1.is_paid)

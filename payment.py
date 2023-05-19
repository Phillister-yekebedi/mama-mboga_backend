class Payments:
    def __init__(self,name,amount, account_number):
        self.name = name
        self.amount  = amount
        self.accout_number = account_number
        # self.payment_status = pending
    def confirm_payment(self):
        print (f"{self.name} your payment is successful")
    def payment_refund_comfirmation(self):
        print (f"{self.name}your refund of{self.amount}is successful")

class MpesaPaymentGateway:
    def process_payment(self, amount, phone_number, pin):
               if self.validate_pin(pin):
                       if self.check_balance(amount):
                        self.deduct_amount(amount)
                        return True
                       else:  
                            return False
                       
    def validate_pin(self, pin):
        return True
    def check_balance(self, amount):
        return True
    def deduct_amount(self, amount):
        print(f"Deducted KES {amount} from user's M-Pesa account.")
class Order:
    def __init__(self, order_number, customer_name, total_price):
        self.order_number = order_number
        self.customer_name = customer_name
        self.total_price = total_price
        self.is_paid = False
    def process_payment(self, payment_gateway, phone_number, pin):
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
    

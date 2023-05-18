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
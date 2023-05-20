class Registration:
    def __init__(self,first_name ,last_name, email, password, password_confirmation):
        self.first_name = first_name 
        self.last_name = last_name
        self.email = email
        self.password= password
        self.password_confirmation= password_confirmation


    def get_customer_details(self) :
         return(f"firstName:{self.first_name},lastName:{self.last_name}")   
         return( f" your name is firstName:{self.first_name},lastName:{self.last_name}and you have just created an account with us")   


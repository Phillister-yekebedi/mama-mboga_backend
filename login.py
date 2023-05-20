class User:
    registered_users = {}
    def __init__(self, user_type, username, password, email):
        self.user_type = user_type
        self.username = username
        self.password = password
        self.email = email
    def register(self):
        self.user_type = input("Enter user type (seller or customer): ")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.email = input("Enter email: ")
        User.registered_users[self.username] = self.password
        new_user = User(self.user_type, self.username, self.password, self.email)
        print("User has registered successfully!")
        return new_user
    def login(self):
        username_input = input("Enter username: ")
        password_input = input("Enter password: ")
        if username_input in User.registered_users and User.registered_users[username_input] == password_input:
            print("Login was successful!")
        else:
            print("Invalid username or password.")
##Instances of a user registering in mama mboga app
user1 = User("customer", "Ruth", "password123", "awinoruthh@gmail.com")
user1.register()
user2 = User("seller", "Awino", "password456", "awinocaren@gmail.com")
user2.register()
##Login instances
user1.login()
user2.login()












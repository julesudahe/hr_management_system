class Password_manager:
    def __init__ (self, latest_password):
        self.latest_password = latest_password 

    def old_password (self):
        old_password_list = []
        for i in range (100):
            old_password_list.append (self.latest_password)
        return old_password_list

    def get_password (self):
        return self.old_password() [-1]

    def set_password (self):
        if self.latest_password != self.get_password():
            self.old_password()
        else: 
            self.get_password()
    
    def is_correct (self):
        self.latest_password = input ('Enter your password: ')
        if self.latest_password in self.get_password ():
            return True
        else:
            return False

e = Password_manager ('jules')

print (e.old_password())
print (e.get_password())
print (e.set_password())
print (e.is_correct())
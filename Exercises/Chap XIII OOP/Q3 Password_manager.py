class Password_manager:
    def __str__(self, latest_password):
        self.latest_password = latest_password 
    def old_password (self):
        old_password_list = []
        for i in range (100):
            old_password_list.append (self.latest_password)
    
    def get_password (self):
        return max (self.old_password())

    def set_password (self):
        
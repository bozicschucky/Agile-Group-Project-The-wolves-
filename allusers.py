class all_users:
    def __init__(self,email,password,role):
        self.email=email
        self.password=password
        self.role=role

    def getEmail(self):
        return self.email;
    def getRole(self):
        return self.role;
    def getPassword(self):
        return self.password;
    def setEmail(self,email):
        self.email=email;
    def setRole(self,role):
        self.role=role;
    def setPassword(self,password):
        self.password=password;
        
        


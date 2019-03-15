class email:
    email=''
    def __init__(self):
        self.email=input('enter email')
    def getuser(self):
        self.u=self.email.split('@')
        print(self.u[0])
    def getdomain(self):
        self.u=self.email.split('@')
        print(self.u[1])

o1=email()
o1.getuser()
o1.getdomain()
    

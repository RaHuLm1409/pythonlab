class employee:
    
    def __init__(self):
        self.firstname=''
        self.lastname=''
        self.salary=0.0
    def set(self):
        self.firstname=input('enter first name')
        self.lastname=input('enter last name')
        self.salary=float(input('enter salary'))
    def get(self):
        print(self.firstname)
        print(self.lastname)
        print(self.salary)
    def check(self):
        if(self.salary<0):
            print('invalid salary')
            self.salary=float(input('enter salary'))
o1=employee()
o1.set()
o1.check()
o1.get()

class rect:
    l=0
    b=0
    def __init__(self):
        self.l=25
        self.b=50
    def calc(self,a):
        r=self.l*self.b
        print(r)
a=rect()
b=rect()
b.calc(a)

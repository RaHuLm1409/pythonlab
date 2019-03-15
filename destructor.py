class des:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print("destructor")
o1=des()
del o1

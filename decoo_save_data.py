#class SavData:
    #def __init__(self, function):
        #self.fun = function()

    #def __call__(self):
        #print("lol")
        #self.fun()
        #print("bol")

def sav_data(fun):
    def wrapper(*args):
        if fun(*args) != None:
            with open('data.txt', 'a') as f:
                f.write(fun(*args)+"\n")

    return wrapper

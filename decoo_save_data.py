
def sav_data(fun):
    def wrapper(*args):
        if fun(*args) != None:
            with open('data.txt', 'a') as f:
                f.write(fun(*args)+"\n")

    return wrapper

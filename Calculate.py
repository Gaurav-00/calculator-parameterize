#pytest install

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
if __name__=="__main__":


    x=int(input("Enter a 1st number"))
    y=int(input("Enter 2nd number"))
    print(add(x,y))
    print(sub(x,y))
    print(mul(x,y))
    print(div(x,y))
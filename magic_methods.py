class Point():
    def __init__(self, x):
        self.x = x
    def __add__(self,other):
        pass
    def __sub__(self,other):
        pass
    def __mul__(self,other):
        pass
    def __mod__(self,other):
        pass
    def __truediv__(self,other):
        pass
    def __floordiv__(self,other):
        pass
    def __pow__(self,other):
        pass


if __name__=="__main__":
    x,y=[int(n) for n in input("Enter 2 integers").split()]
    p1=Point(x)
    p2=Point(y)
    print(p1 + p2)
    print(p1 - p2)
    print(p1 * p2)
    print(p1 % p2)
    print(p1 / p2)
    print(p1 // p2)
    print(p1 ** p2)

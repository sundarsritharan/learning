class CountFromBy:

    def __init__(self,v:int=0,i:int=1) -> None:
        """ initialize the class """ 
        self.val = v
        self.incr = i

    def increase(self) -> None:
        """ increase the value of the given number """ 
        self.val += self.incr 
     
    def __repr__(self) -> None:
        """ overriding default representation of the object """
        return str(self.val)    


h = CountFromBy()
print(h.val)
print(h.incr)
h.increase()
print(h)
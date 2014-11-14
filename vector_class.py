import math

class Vector:

    def __init__(self,arr):
        self.arr = arr

    def __str__(self):
        return filter(lambda x: not x.isspace(),str(tuple(self.arr)))

    def add(self, other):
        return Vector([x+y for x,y in zip(self.arr,other.arr)])

    def subtract(self,other):
        return Vector([x-y for x,y in zip(self.arr,other.arr)])

    def dot(self,other):
        return reduce(lambda x,y: x+y,[x*y for x,y in zip(self.arr,other.arr)])

    def norm(self):
        return math.sqrt(reduce(lambda x,y: x+y,map(lambda x: x*x, self.arr)))
    
    def equals(self,other):
        return self.arr == other.arr




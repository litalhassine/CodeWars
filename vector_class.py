class Vector:

    def __init__(self,arr):
        self.arr = arr

    def __str__(self):
        return str(self.arr)

    def add(self, other):
        return Vector([x+y for x,y in zip(self.arr,other.arr)])

    def substract(self,other):
        return Vector([x-y for x,y in zip(self.arr,other.arr)])

    def dot(self,other):
        return Vector(reduce(lambda x,y: x+y,[x*y for x,y in zip(self.arr,other.arr)]))
    
    def equals(self,other):
        return self.arr == other.arr




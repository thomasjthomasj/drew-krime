import math

class Vector:
    
    @staticmethod
    def magnitude(v):
        return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

    @staticmethod
    def add(u, v):
        return [ u[i]+v[i] for i in range(len(u)) ]
    
    @staticmethod
    def sub(u, v):
        return [ u[i]-v[i] for i in range(len(u)) ]    

    @staticmethod
    def dot(u, v):
        return sum(u[i]*v[i] for i in range(len(u)))

    @staticmethod
    def normalize(v):
        vmag = Vector.magnitude(v)
        return [ v[i]/vmag  for i in range(len(v)) ]
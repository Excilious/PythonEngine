"""
Copyright (C) 2024 Excilious

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

from ConfigurationsBinder import *

class Collision3D:
    def __init__(self): ...

    def CollisionPoint(self,Object1,Object2):
        if (Object1.Position == Object2.Position):
            return True
        return False

    def CollisionBox(self,Object1,Object2,NoForceApplied):
        if (Object1.InstanceName in NoForceApplied):
            if (
                Object1.Position.x < Object2.Position.x + Object2.Scale.x and
                Object1.Position.x + Object1.Scale.x > Object2.Position.x and 
                Object1.Position.y < Object2.Position.y + Object2.Scale.y and 
                Object1.Position.y + Object1.Scale.y > Object2.Position.y and
                Object1.Position.z < Object2.Position.z + Object2.Scale.z and 
                Object1.Position.z + Object1.Scale.z > Object2.Position.z
                ):
                return True
            else:
                return False
        return False
    
    def CollisionMesh(self,Object1,Object2):
        ...

    def CollidedSphere(self,Object1,Object2):
        ...
    

class CreateBoundingBox:
    def __init__(self,BoundMin,BoundMax,Radius):
        self.BoundMin = BoundMin
        self.BoundMax = BoundMax
        self.BoundCenter = (self.BoundMin + self.BoundMax) * 0.5
        self.Radius = Radius
        
    def CheckCollision(self,Position,Scale=1.0):
        return  numpy.all(((self.BoundCenter + (self.BoundMin - self.BoundCenter) * Scale) <= Position) and
                numpy.all(Position <= (self.BoundCenter + (self.BoundMax - self.BoundCenter) * Scale))
        )
    
    def UpdateBoundBox(self):
        self.BoundCenter = (self.BoundMin + self.BoundMax) * 0.5
        self.Radius = (self.BoundMax - self.BoundMin)

    def UpdateBoundMatrix(self,BoundaryBox,Matrix):
        BoundMin = numpy.dot(numpy.array([BoundaryBox.BoundMin,BoundaryBox.BoundMin,BoundaryBox.BoundMin,1.0],dtype=numpy.float32),Matrix)[:3]
        BoundMax = numpy.dot(numpy.array([BoundaryBox.BoundMax,BoundaryBox.BoundMax,BoundaryBox.BoundMax,1.0],dtype=numpy.float32),Matrix)[:3]
        self.BoundMin = numpy.minimum(BoundMin, BoundMax)
        self.BoundMax = numpy.maximum(BoundMin, BoundMax)
        self.BoundCenter = (self.BoundMin + self.BoundMax) * 0.5
        self.Radius = (self.BoundMax - self.BoundMin)

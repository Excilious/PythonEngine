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

class CollisionBox:
    def __init__(self):
        self.MaximumPoint = None
        self.MinimumPoint = None

    def IsCollided(self,OtherCollision):
        return (self.MinimumPoint[0] <= OtherCollision.MaximumPoint[0] and 
                self.MaximumPoint[0] >= OtherCollision.MinimumPoint[0] and 
                self.MinimumPoint[1] <= OtherCollision.MaximumPoint[1] and
                self.MaximumPoint[1] >= OtherCollision.MinimumPoint[1] and
                self.MinimumPoint[2] <= OtherCollision.MaximumPoint[2] and
                self.MaximumPoint[2] >= OtherCollision.MinimumPoint[2]
                )
    
    def CreateCollisionBox(self,MeshID):
        MinimumPoint = [float('inf'),float('inf'),float('inf')]
        MaximumPoint = [-float('inf'),-float('inf'),-float('inf')]

        NewObject = pywavefront.Wavefront(MeshID,cache=True,parse=True)
        for Vertex in NewObject.vertices:
            for x in range(3):
                MinimumPoint[x] = min(MinimumPoint[x],Vertex[x])
                MaximumPoint[x] = max(MaximumPoint[x],Vertex[x])
        
        self.MaximumPoint = MaximumPoint
        self.MinimumPoint = MinimumPoint

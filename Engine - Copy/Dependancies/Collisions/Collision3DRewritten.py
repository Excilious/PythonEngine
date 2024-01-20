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
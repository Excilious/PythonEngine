from ConfigurationsBinder import *
from Dependancies.Support.SupportLibrary import *
from Dependancies.Collisions.Collision3D import *

class Physics:
    def __init__(self,Application,SceneParts):
        self.NoForceApplied = []
        self.CoreProperties = {}
        self.Application = Application
        self.CollisionLibrary = Collision3D()
        
        self.NoForce("Baseplate")
        self.NoForce("Squidward")
        self.NoForce("PlayerInstance")
        self.ApplyCoreProperties("CharacterHumanoid","PlayerObject",True)

        self.Velocity = OBJECT_VELOCITY
        self.FinalVelocity = OBJECT_VELOCITY * self.Application.DeltaTime
        self.SceneParts = SceneParts

    def NoForce(self,NameNoForce):
        self.NoForceApplied.append(NameNoForce)

    def ApplyCoreProperties(self,CoreBase,NameKey,Argument):
        self.CoreProperties[CoreBase] = {}
        self.CoreProperties[CoreBase][NameKey] = Argument

    def GetScene(self,SceneBricks):
        self.SceneParts = SceneBricks

    def OnPartCollisions(self,SceneParts):   
        for Object1 in SceneParts:
            for Object2 in SceneParts:
                if (Object1.InstanceName != Object2.InstanceName):
                    print(str(Object1.InstanceName)+" to "+str(Object2.InstanceName)+": - "+ str(Object1.Collision.IsCollided(Object2.Collision)))
                    if (Object1.Collision.IsCollided(Object2.Collision)):
                        self.NoForceApplied.append(Object1.InstanceName)
                        self.NoForceApplied.append(Object2.InstanceName)

                # if (Object1.InstanceName != Object2.InstanceName and self.CollisionLibrary.CollisionBox(Object1,Object2,self.NoForceApplied)):
                #     if (Object1.InstanceName not in self.NoForceApplied and Object2.InstanceName not in self.NoForceApplied):
                #         print(str(Object1.InstanceName)+" touched  "+str(Object2.InstanceName))
                #         self.Velocity = -self.Velocity


    def Update(self,SceneParts):
        self.SceneParts = SceneParts
        for Objects in SceneParts:
            if (Objects.InstanceName == "Squidward"):
                Objects.Rotation += glm.vec3(0,0.04,0)

            if not (Objects.InstanceName in self.NoForceApplied):
                if (Objects.Position.y >= 200):
                    self.Velocity = OBJECT_VELOCITY

                self.FinalVelocity = self.Velocity * self.Application.DeltaTime
                Objects.Position -= glm.vec3(0,1,0) * self.FinalVelocity

        self.OnPartCollisions(SceneParts)
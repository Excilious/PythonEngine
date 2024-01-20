from ConfigurationsBinder import *
from Enviroments.VertexBufferObject import *
from Enviroments.VertexArrayObject import *

from Dependancies.Collisions.Collision3D import *
from Dependancies.Collisions.Collision3DRewritten import *

class Model:
    Array = None

    def __init__(self,Application,VertexArrayName,MeshID,TextureID="1",Position = MODEL_POSITION,Rotation = MODEL_ROTATION,Scale = MODEL_SCALE):
        self.Application = Application
        self.VertexArrayName = VertexArrayName
        self.VertexArrayDude = None
        self.VertexArray = self.Application.Mesh.VertexArrayObject

        self.Position = Position
        self.Rotation = glm.vec3([glm.radians(Value) for Value in Rotation])
        self.Scale = Scale
        self.Collision = CollisionBox()

        if (MeshID): 
            self.SetMeshID(MeshID)
            self.Collision.CreateCollisionBox(MeshID)
        else:
            self.Collision.MinimumPoint = glm.vec3(0,0,0)
            self.Collision.MaximumPoint = Scale

        print(self.Collision.MinimumPoint,self.Collision.MaximumPoint)
        self.CollisionBox = CreateBoundingBox(self.Position.y-(self.Scale.y/2),self.Position.y+(self.Scale.y/2),self.Position.x+(self.Scale.x/2))
        self.MatrixModel = self.GetModelMatrix()
        self.TextureID = TextureID

        self.VertexArray = self.VertexArray.VertexArrays[VertexArrayName]
        self.NewVertexArray = None

        self.Program = self.VertexArray.program
        self.Camera = self.Application.Camera

    def SetMeshID(self,MeshID):
        self.VertexBufferCreation = VertexBuffer(self.Application.Context)
        self.VertexArray = self.Application.Mesh.VertexArrayObject
        Array = self.VertexArray.AddNewArray(self.VertexArrayName,'Default',MeshID)
        Model.Array = Array

    def Update(self):
        ...

    def GetModelMatrix(self):
        ModelMatrix = glm.mat4()

        ModelMatrix = glm.translate(ModelMatrix, self.Position)
        ModelMatrix = glm.rotate(ModelMatrix,self.Rotation.z, glm.vec3(0,0,1))
        ModelMatrix = glm.rotate(ModelMatrix,self.Rotation.y, glm.vec3(0,1,0))
        ModelMatrix = glm.rotate(ModelMatrix,self.Rotation.x, glm.vec3(1,0,0))

        ModelMatrix = glm.scale(ModelMatrix, self.Scale)
        # self.CollisionBox.UpdateBoundMatrix(self.CollisionBox,ModelMatrix)
        return ModelMatrix
    
    def Render(self):
        self.Update()
        if (Model.Array):
            Model.Array[self.VertexArrayName].render()

class ModelConstructor(Model):
    def __init__(self,Application,VertexArrayName,MeshID,TextureID,Position,Rotation,Scale):
        super().__init__(Application,VertexArrayName,MeshID,TextureID,Position,Rotation,Scale)
        self.Start()

    def Update(self):
        self.Texture.use(location=0)
        self.Program['CameraPosition'].write(self.Camera.Position)
        self.Program['MatrixView'].write(self.Camera.ViewMatrix)
        self.Program['MatrixModel'].write(self.MatrixModel)

    def UpdateShadow(self):
        self.ShadowMapProgram['MatrixModel'].write(self.MatrixModel)

    def RenderShadow(self):
        self.UpdateShadow()
        self.ShadowMapArray.render()

    def Start(self):
        self.ShadowMapArray = self.Application.Mesh.VertexArrayObject.VertexArrays[self.VertexArrayName]
        self.ShadowMapProgram = self.ShadowMapArray.program
        self.ShadowMapProgram['MatrixProjection'].write(self.Camera.ProjectionMatrix)
        self.ShadowMapProgram['MatrixViewLight'].write(self.Application.Lighting.ViewLightMatrix)
        self.ShadowMapProgram['MatrixModel'].write(self.MatrixModel)

        self.Program['MatrixViewLight'].write(self.Application.Lighting.ViewLightMatrix)
        self.Program['Resolution'].write(RESOLUTION)
        self.DepthTexture = self.Application.Mesh.Texture.Textures['DepthTexture']
        self.Program['ShadowMap'] = 1
        self.DepthTexture.use(location=1)

        self.Texture = self.Application.Mesh.Texture.Textures[self.TextureID]
        self.Program['Texture'] = 0
        self.Texture.use(location=0)

        self.Program['MatrixProjection'].write(self.Camera.ProjectionMatrix)
        self.Program['MatrixView'].write(self.Camera.ViewMatrix)
        self.Program['MatrixModel'].write(self.MatrixModel)

        self.Program['light.LightingPosition'].write(self.Application.Lighting.Position)
        self.Program['light.LightingAmbience'].write(self.Application.Lighting.LightingAmbience)
        self.Program['light.LightingDiffusion'].write(self.Application.Lighting.LightingDiffusion)
        self.Program['light.LightingSpecular'].write(self.Application.Lighting.LightingSpecular)

class SkyBox(Model):
    def __init__(self,Application,VertexArrayName='Skybox',TextureID='Skybox'):
        super().__init__(Application,VertexArrayName,None,TextureID)
        self.Start()
    
    def Update(self):
        MatrixView = glm.mat4(glm.mat3(self.Camera.ViewMatrix))
        self.Program['ProjectionInverseView'].write(glm.inverse(self.Camera.ProjectionMatrix * MatrixView))

    def Start(self):
        self.Texture = self.Application.Mesh.Texture.Textures[self.TextureID]
        self.Program['TextureSkybox'] = 0
        self.Texture.use(location=0)

class MeshBrickModel(ModelConstructor):
    def __init__(self,Application,WorldSpaceName,MeshID,VertexArrayName='MeshBrick',TextureID=1,Position=glm.vec3(0,0,0),Rotation=glm.vec3(-90,0,0),Scale=glm.vec3(1,1,1)):
        assert(WorldSpaceName,"WorldSpaceName would be needed to create the instance!")
        assert(MeshID, "MeshID would be required to create a mesh!")
        super().__init__(Application,VertexArrayName,MeshID,TextureID,Position,Rotation,Scale)
        self.InstanceName = WorldSpaceName

    def Update(self):
        self.MatrixModel = self.GetModelMatrix()
        super().Update()

class PartBrickModel(ModelConstructor):
    def __init__(self,Application,WorldSpaceName,VertexArrayName='PartBrick',TextureID=1,Position=glm.vec3(0,0,0),Rotation=glm.vec3(-90,0,0),Scale=glm.vec3(1,1,1)):
        assert(WorldSpaceName,"WorldSpaceName would be needed to create the instance!")
        super().__init__(Application,VertexArrayName,None,TextureID,Position,Rotation,Scale)
        self.InstanceName = WorldSpaceName

    def Update(self):
        self.MatrixModel = self.GetModelMatrix()
        super().Update()
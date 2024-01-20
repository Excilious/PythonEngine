from Enviroments.Shader import *
from Enviroments.VertexBufferObject import *

class VertexArray:
    def __init__(self,Context,NewVertexBuffer=None):
        if (not NewVertexBuffer): NewVertexBuffer = VertexBuffer(Context)

        self.Context = Context
        self.VertexBuffer = VertexBuffer(Context)
        self.Programs = Shader(Context)

        self.VertexArrays = {}

        self.VertexArrays['MeshBrick'] = self.GetVertexArray(
            Program = self.Programs.Programs['Default'],
            VertexBuffer = self.VertexBuffer.VertexBuffers['MeshBrick'],
        )
        self.VertexArrays['PartBrick'] = self.GetVertexArray(
            Program = self.Programs.Programs['Default'],
            VertexBuffer = self.VertexBuffer.VertexBuffers['PartBrick'],
        )
        self.VertexArrays['Skybox'] = self.GetVertexArray(
            Program=self.Programs.Programs['Skybox'],
            VertexBuffer = self.VertexBuffer.VertexBuffers['Skybox'],
        )
        # self.VertexArrays['ShadowPartBrick'] = self.GetVertexArray(
        #     Program = self.Programs.Programs['ShadowMap'],
        #     VertexBuffer = self.VertexBuffer.VertexBuffers['PartBrick'],
        # )

    def AddNewArray(self,InstanceName,Shader,MeshID):
        self.VertexBuffer.VertexBuffers = self.VertexBuffer.PlsCreateDude(self.Context,InstanceName,MeshID)
        self.VertexArrays[InstanceName] = self.GetVertexArray(
                Program = self.Programs.Programs[Shader],
                VertexBuffer = self.VertexBuffer.VertexBuffers[InstanceName],
            )
        return self.VertexArrays
        
    def GetVertexArray(self,Program,VertexBuffer):
        VertexArrayObject = self.Context.vertex_array(Program,[
            (VertexBuffer.VertexBuffer, VertexBuffer.Format, *VertexBuffer.Attributes)
        ],
        skip_errors=True)
        return VertexArrayObject
    
    def Destroy(self):
        self.VertexBuffer.Destroy()
        self.Programs.Destroy()
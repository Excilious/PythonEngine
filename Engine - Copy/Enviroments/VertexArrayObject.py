"""
Script has been rewritten to fit within the certain purpose given, however most of the codebase remains the same to the original 
author.

MIT License

Copyright (c) 2023 StanislavPetrovV

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


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

from ConfigurationsBinder import *

class Shader:
    def __init__(self,Context):
        self.Context = Context
        self.Programs = {}

        self.Programs['Default'] = self.GetProgram('Default')
        self.Programs['Skybox'] = self.GetProgram('Skybox')
        self.Programs['ShadowMap'] = self.GetProgram('ShadowMap')
    
    def GetProgram(self,ShaderName):
        with open(f'./Shaders/{ShaderName}.vert') as Vertices:
            VertexShader = Vertices.read()
        
        with open(f'./Shaders/{ShaderName}.frag') as Fragments:
            FragmentShader = Fragments.read()

        Program = self.Context.program(vertex_shader=VertexShader, fragment_shader=FragmentShader)
        return Program

    def Destroy(self):
        [Program.release() for Program in self.Programs.values()]
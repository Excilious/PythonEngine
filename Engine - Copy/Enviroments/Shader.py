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

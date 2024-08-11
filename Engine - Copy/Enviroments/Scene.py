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


from Enviroments.Models import *
from Enviroments.Meshes import *
from Enviroments.VertexArrayObject import *
from ConfigurationsBinder import *

from Dependancies.Physics.Physics import *
from Dependancies.Model3D.Model3DGeneration import *

class Scene:
    SceneParts = []
    CharacterFocus = None

    def __init__(self,Application):
        self.Application = Application
        self.Objects = []
        self.ProtectedApplications = []

        self.Model3D = Model3DGeneration(Application)
        self.Mesh = Mesh(Application)
        self.Physics = Physics(Application,Scene.SceneParts)

        self.Load()
        self.Skybox = SkyBox(Application)
        self.DepthTexture = self.Mesh.Texture.Textures['DepthTexture']
        self.DepthBuffer = self.Application.Context.framebuffer(depth_attachment=self.DepthTexture)

    def AddObjects(self,Object,Protected=None):
        if (Protected):
            self.ProtectedApplications.append(Object)
        self.Objects.append(Object)
        Scene.SceneParts.append(Object)

    def Load(self):
        self.PlayerObject = PartBrickModel(self.Application,WorldSpaceName="PlayerInstance",Position=glm.vec3(0,0,0),Scale=glm.vec3(1,1,1))
        self.AddObjects(self.PlayerObject)
        Scene.CharacterFocus = self.PlayerObject

        self.Baseplate = PartBrickModel(self.Application,WorldSpaceName="Baseplate",Position=glm.vec3(0,0,0),Scale=glm.vec3(10,10,0.2))
        self.AddObjects(self.Baseplate)

        self.Squidward = MeshBrickModel(self.Application,WorldSpaceName="Squidward",MeshID="./Meshes/Squid.obj",TextureID="Squidward",VertexArrayName="Squidward",Rotation=glm.vec3(0,90,0),Position=glm.vec3(0,0,0),Scale=glm.vec3(0.25,0.25,0.25))
        self.AddObjects(self.Squidward)

        self.PartBrick = PartBrickModel(self.Application,WorldSpaceName="PartBrick",Position=glm.vec3(0,100,0),Scale=glm.vec3(1,1,1))
        self.AddObjects(self.PartBrick)

    def Generate3DModel(self):
        CharacterModel = self.Model3D.SetCharacter()
        for Bones in CharacterModel.keys():
            self.AddObjects(CharacterModel[Bones])

    def Update(self):
        self.Physics.Update(Scene.SceneParts)

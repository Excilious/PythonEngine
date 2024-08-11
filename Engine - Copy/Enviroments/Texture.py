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

class Texture:
    def __init__(self,Application):
        self.Application = Application
        self.Context = Application.Context
        self.Textures = {}

        self.Textures[1] = self.GetTextures(Path=f'./Textures/Baseplate.png')
        self.Textures[2] = self.GetTextures(Path=f'./Textures/Baseplate.png')
        self.Textures["Dude"] = self.GetTextures(Path=f'./Textures/DiffusionTest.png')
        self.Textures["Squidward"] = self.GetTextures(Path=f'./Textures/Squidward.png')

        self.Textures['Skybox'] = self.GetTextureCube(Path=f'./Textures/Skybox/')
        self.Textures['DepthTexture'] = self.GetDepthTexture()

    def GetDepthTexture(self):
        DepthTexture = self.Context.depth_texture((int(RESOLUTION.x),int(RESOLUTION.y)))
        return DepthTexture
    
    def GetTextureCube(self,Path,Extention='png'):
        GetFaces = ['Right','Left','Top','Bottom'] + ['Front','Back'][::-1]
        Textures = []

        for Face in GetFaces:
            NewTexture = pygame.image.load(Path + f'{Face}.{Extention}').convert()
            if (Face in ['Right','Left','Front','Back']):
                Texture = pygame.transform.flip(NewTexture,flip_x=True,flip_y=False)
            else:
                Texture = pygame.transform.flip(NewTexture,flip_x=False,flip_y=True)
            Textures.append(Texture)
        
        Size = Textures[0].get_size()
        TextureCube = self.Context.texture_cube(size=Size,components=3,data=None)

        for Index in range(6):
            TextureData = pygame.image.tostring(Textures[Index],'RGB')
            TextureCube.write(face=Index,data=TextureData)

        return TextureCube
    
    def GetTextures(self,Path):
        Texture = pygame.image.load(Path).convert()
        Texture = pygame.transform.flip(Texture, flip_x=False,flip_y=True)
        Texture = self.Context.texture(size=Texture.get_size(),components=3,data=pygame.image.tostring(Texture,'RGB'))

        Texture.filter = (moderngl.LINEAR_MIPMAP_LINEAR, moderngl.LINEAR)
        Texture.build_mipmaps()
        Texture.anisotropy = 32.0
        return Texture
    
    def Destroy(self):
        [Texture.release() for Texture in self.Textures.values()]

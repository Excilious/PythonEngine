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


class Renderer:
    def __init__(self,Application):
        self.Application = Application
        self.Context = Application.Context
        self.Mesh = Application.Mesh
        self.Scene = Application.Scene

        self.Texture = self.Mesh.Texture.Textures['DepthTexture']
        self.Depth = self.Context.framebuffer(depth_attachment=self.Texture)

    def RenderShadow(self):
        self.Depth.clear()
        self.Depth.use()
        for Object in self.Scene.Objects:
            Object.RenderShadow()

    def RenderEnviroment(self):
        self.Application.Context.screen.use()
        for Object in self.Scene.Objects:
            Object.Render()
        self.Scene.Skybox.Render()

    def Render(self):
        self.Scene.Update()
        self.RenderShadow()
        self.RenderEnviroment()

    def Destroy(self):
        self.Depth.release()

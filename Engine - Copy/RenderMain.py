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
from Enviroments.Camera import *
from Enviroments.Lighting import *
from Enviroments.Meshes import *
from Enviroments.Scene import *
from Enviroments.Render import *

from Dependancies.Physics.Physics import *
from Dependancies.Model3D.Model3DGeneration import *
from Dependancies.Model3D.CharacterSkeleton import *

class MainEngine:
    def __init__(self):
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION,3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION,3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        pygame.display.set_mode(RESOLUTION,flags=pygame.OPENGL | pygame.DOUBLEBUF)

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

        self.Context = moderngl.create_context()
        self.Context.enable(flags=moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        self.Clock = pygame.time.Clock()
        self.DeltaTime = 0
        self.Time = 0 
        
        self.Lighting = Lighting()
        self.Camera = Camera(self)
        self.Mesh = Mesh(self)
        self.Scene = Scene(self)
        self.Renderer = Renderer(self)

        self.Physics = Physics(self,self.Scene.SceneParts)

    def EventsBinder(self):
        for Event in pygame.event.get():
            if (Event.type == pygame.QUIT or (Event.type == pygame.KEYDOWN and Event.key == pygame.K_ESCAPE)):
                self.Mesh.Destroy()
                self.Renderer.Destroy()
                pygame.quit()
                sys.exit()

    def RenderBinder(self):
        self.Context.clear(color=BACKGROUND_COLOUR)
        self.Renderer.Render()
        pygame.display.flip()

    def UpdateBinder(self):
        self.Time = pygame.time.get_ticks() * 0.001
    
    def Run(self):
        while True:
            self.UpdateBinder()
            self.EventsBinder()
            self.Camera.Update()
            self.RenderBinder()
            self.DeltaTime = self.Clock.tick(MAX_FPS)
            pygame.display.set_caption("FPS: "+str(int(self.Clock.get_fps()))+ "  Camera Pos: "+str(self.Camera.Position))
        
if (__name__ == '__main__'):
    Engine = MainEngine()
    Engine.Run()

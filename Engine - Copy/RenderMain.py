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
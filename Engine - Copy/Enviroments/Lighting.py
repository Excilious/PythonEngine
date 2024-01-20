from ConfigurationsBinder import *

class Lighting:
    def __init__(self,Position=LIGHT_POSITION,Colour=LIGHT_COLOUR):
        self.Position = Position
        self.Colour = Colour
        self.Direction = glm.vec3(0,0,0)

        self.LightingAmbience = LIGHT_AMBIENCE * self.Colour
        self.LightingDiffusion = LIGHT_DIFFUSION * self.Colour
        self.LightingSpecular = LIGHT_SPECULAR * self.Colour

        self.ViewLightMatrix = self.GetViewLightMatrix()

    def GetViewLightMatrix(self):
        return glm.lookAt(self.Position, self.Direction, glm.vec3(0,1,0))
    
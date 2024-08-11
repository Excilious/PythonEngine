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
    

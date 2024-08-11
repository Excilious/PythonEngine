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
from Dependancies.Physics.Physics import *
from Enviroments.Scene import *

class Camera(Physics):
    def __init__(self,Application,Position=CAMERA_POSITION,YRotation=CAMERA_Y,XRotation=CAMERA_X):
        super().__init__(Application,Scene.SceneParts)

        self.Application = Application
        self.CameraViewRatio = RESOLUTION.x / RESOLUTION.y
        self.Position = Position
        
        self.CameraUp = glm.vec3(0,1,0)
        self.CameraRight = glm.vec3(1,0,0)
        self.CameraForward = glm.vec3(0,0,-1)
        
        self.RotationX = XRotation
        self.RotationY = YRotation

        self.Scenes = []

        self.ViewMatrix = self.GetViewMatrix()
        self.ProjectionMatrix = self.GetProjectionMatrix()

    def RotateCamera(self):
        RelX,RelY = pygame.mouse.get_rel()
        self.RotationY += RelX * SENSITIVITY
        self.RotationX -= RelY * SENSITIVITY
        self.RotationX = max(-89, min(89, self.RotationX))

    def UpdateCamera(self):
        RotateY,RotateX = glm.radians(self.RotationY),glm.radians(self.RotationX)

        self.CameraForward.x = glm.cos(RotateY) * glm.cos(RotateX)
        self.CameraForward.y = glm.sin(RotateX)
        self.CameraForward.z = glm.sin(RotateY) * glm.cos(RotateX)

        self.CameraForward = glm.normalize(self.CameraForward)
        self.CameraRight = glm.normalize(glm.cross(self.CameraForward, glm.vec3(0,1,0)))
        self.Up = glm.normalize(glm.cross(self.CameraRight, self.CameraForward))

    def MoveForward(self,Velocity):
        return self.CameraForward.xz * Velocity
    
    def MoveBackward(self,Velocity):
        return -self.CameraForward.xz * Velocity
    
    def MoveLeft(self,Velocity):
        return -self.CameraRight.xz * Velocity
    
    def MoveRight(self,Velocity):
        return self.CameraRight.xz * Velocity
        
    def Move(self):
        Velocity = SPEED * self.Application.DeltaTime
        Keys = pygame.key.get_pressed()
        NewStep = glm.vec2()
        
        if (Keys[pygame.K_w]):
            NewStep += self.MoveForward(Velocity)
        if (Keys[pygame.K_s]):
            NewStep += self.MoveBackward(Velocity)
        if (Keys[pygame.K_a]):
            NewStep += self.MoveLeft(Velocity)
        if (Keys[pygame.K_d]):
            NewStep += self.MoveRight(Velocity)

        if (DEBUG):
            if (Keys[pygame.K_q]):
                self.Position += self.CameraUp * Velocity
            if (Keys[pygame.K_e]):
                self.Position -= self.CameraUp * Velocity

        self.CollisionMove(NewStep)

    def CollisionMove(self,NewStep):
        self.Position.x += NewStep[0]
        self.Position.z += NewStep[1]
    
    def GetViewMatrix(self):
        return glm.lookAt(self.Position, self.Position + self.CameraForward, self.CameraUp)

    def GetProjectionMatrix(self):
        return glm.perspective(glm.radians(FIELD_OF_VIEW), self.CameraViewRatio, NEAR_VIEW,FAR_VIEW)

    def Update(self):
        Scene.CharacterFocus.Position = self.Position
        self.Move()
        self.RotateCamera()
        self.UpdateCamera()
        self.ViewMatrix = self.GetViewMatrix()

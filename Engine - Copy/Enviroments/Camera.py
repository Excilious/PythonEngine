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

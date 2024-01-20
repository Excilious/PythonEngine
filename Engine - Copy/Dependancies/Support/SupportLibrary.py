from ConfigurationsBinder import *

class Tween:
    TweenInstances = {}

    def Create(self,Name,EndPosition,ObjectInstance,TweenSpeed):

        if (Name in Tween.TweenInstances.keys()):
            print(f"Tween has already been created with the name {Name}. Please choose a different name.")
        else:
            Tween.TweenInstances[Name] = {}

        if (not EndPosition.x and
            not EndPosition.y and 
            not EndPosition.z):
            print("EndPosition must be in vector3 format.")
            Tween.TweenInstances[Name] = None
            return None

        Tween.TweenInstances[Name]["PositionalObject"] = EndPosition
        Tween.TweenInstances[Name]["ObjectInstance"] = ObjectInstance
        Tween.TweenInstances[Name]["Speed"] = TweenSpeed
        Tween.TweenInstances[Name]["IsRunning"] = True
 
    def Start(self,Name):
        if (not Tween.TweenInstances[Name]):
            print("TweenName would not be found within the tweeninstance.")
            return None
        
        FinalPosition = Tween.TweenInstances[Name]["PositionalObject"]
        ObjectToRender = Tween.TweenInstances[Name]["ObjectInstance"]
        SpeedIncrement = Tween.TweenInstances[Name]["Speed"]
        SpeedX,SpeedY,SpeedZ = SpeedIncrement,SpeedIncrement,SpeedIncrement
        
        if (ObjectToRender.Position.x < 0):
            SpeedX = -SpeedX
        else:
            SpeedX = +SpeedX

        if (ObjectToRender.Position.y < 0):
            SpeedY = -SpeedY
        else:
            SpeedY = +SpeedY

        if (ObjectToRender.Position.z < 0):
            SpeedZ = -SpeedZ
        else:
            SpeedZ = +SpeedZ

        for x in numpy.arange(ObjectToRender.Position.x,FinalPosition.x,SpeedX):
            for y in numpy.arange(ObjectToRender.Position.y,FinalPosition.y,SpeedY):
                for z in numpy.arange(ObjectToRender.Position.z,FinalPosition.z,SpeedZ):
                    if (not Tween.TweenInstances[Name]["IsRunning"]): break
                    ObjectToRender.Position = glm.vec3(x,y,z)

    def Stop(self,Name):
        if (Name not in Tween.TweenInstances.keys()):
            print(f"Tween ({Name}) has not be created and therefore cannot be stopped.")
        
        Tween.TweenInstances[Name]["IsRunning"] = False

class InputService:
    TrackInput = []
    IsTracking = False

    def StartTracking(self):
        if (InputService.IsTracking): return

        InputService.IsTracking = True
        if (pygame.event == pygame.KEYDOWN):
            InputService.TrackInput.append(pygame.key.get_pressed())

    def StopTracking(self):
        InputService.IsTracking = False
        InputService.TrackInput = []

    def GetAllTracked(self):
        return InputService.TrackInput
    
class DataStorage:
    def GetData(self,DataName):
        NewData = None
        with open(f'./Dependancies/{DataName}.lds') as UserData:
            NewData = UserData.readline()

    def SaveData(self,DataName):
        ...

class SupportLibrary:
    def __init__(self):
        try:
            self.Services = {
                "TweenService":Tween()
            }
        except Exception as Error:
            print(f'SupportLibrary failed to initilise. Reason: {Error}')



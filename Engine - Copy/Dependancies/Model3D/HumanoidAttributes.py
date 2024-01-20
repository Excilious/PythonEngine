from ConfigurationsBinder import *

class HumanoidAttributes:
    def __init__(self):
        self.ToolCameraOffset = glm.vec3(0,0,0)

    def AttachNewTool(self,Object):
        #Tool must be rerendered within a rendering system.
        #TODO: Create tool character animaton (Could replicate towards the server)
        self.Object.Position = CAMERA_POSITION + self.ToolCameraOffset

        
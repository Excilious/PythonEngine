"""
Copyright (C) 2024 Excilious

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

from ConfigurationsBinder import *

class HumanoidAttributes:
    def __init__(self):
        self.ToolCameraOffset = glm.vec3(0,0,0)

    def AttachNewTool(self,Object):
        #Tool must be rerendered within a rendering system.
        #TODO: Create tool character animaton (Could replicate towards the server)
        self.Object.Position = CAMERA_POSITION + self.ToolCameraOffset

        

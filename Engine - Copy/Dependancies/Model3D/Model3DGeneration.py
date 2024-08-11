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

from Enviroments.Models import *

class Model3DGeneration:
    def __init__(self,Application):
        self.Application = Application

    def SetCharacter(self):
        #Attachments are binded to ChestTorso. Position from there.
        self.Bones = {}
        self.ScaleModifier = 1

        CharacterMapAttributes = {
            "LeftArm":{
                    "Scale":glm.vec3(0,0,0),
                    "Position":glm.vec3(0,0,0)
                },
            "RightArm":{
                    "Scale":glm.vec3(0,0,0),
                    "Position":glm.vec3(0,0,0)
                },
            "LeftLeg":{
                    "Scale":glm.vec3(0.1,0.1,0.5),
                    "Position":glm.vec3(0,-0.5,0.15)
                },
            "RightLeg":{
                    "Scale":glm.vec3(0.1,0.1,0.5),
                    "Position":glm.vec3(0,-0.5,-0.15)
                },
            "ChestTorso":{
                    "Scale":glm.vec3(0,0,0),
                    "Position":glm.vec3(0,0,0)
                },
            "HipTorso":{
                    "Scale":glm.vec3(0,0,0),
                    "Position":glm.vec3(0,0,0)
                },
            "Head":{
                    "Scale":glm.vec3(0.15,0.15,0.15),
                    "Position":glm.vec3(0,0.5,0)
                }
        }

        for Bone in CharacterMapAttributes.keys():
            print(Bone)
            self.Bones[Bone] = PartBrickModel(self.Application,
                                        WorldSpaceName=str(Bone),
                                        Position=CharacterMapAttributes[Bone]["Position"],
                                        Scale=CharacterMapAttributes[Bone]["Scale"] * self.ScaleModifier       
                                              )
        
        return self.Bones

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
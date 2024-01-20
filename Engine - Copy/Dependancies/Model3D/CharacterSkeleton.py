from ConfigurationsBinder import *

class Skeleton:
    SkeletonMap = {}
    JointMap = {
        "HipTorso":"ChestTorso",
        
        "LeftArm":"ChestTorso",
        "RightArm":"ChestTorso",
        "LeftLeg":"HipTorso",
        "RightLeg":"HipTorso",

        "Head":"ChestTorso",
    }

    def __init__(self,Model,CharacterSkeleton):
        Skeleton.SkeletonMap[Model.InstanceName] = {}
        Skeleton.SkeletonMap[Model.InstanceName]["Bones"] = {}
        Skeleton.SkeletonMap[Model.InstanceName]["Joints"] = {}

        for Bones in CharacterSkeleton.keys():
            if (Bones in Skeleton.JointMap.keys()):
                Skeleton.SkeletonMap[Model.InstanceName]["Joints"][Skeleton.JointMap[Bones]] = {
                    "Joint1": CharacterSkeleton[Skeleton.JointMap[Bones]],
                    "Joint2": CharacterSkeleton[Bones]
                }

            Skeleton.SkeletonMap[Model.InstanceName]["Bones"][Bones] = CharacterSkeleton[Bones]


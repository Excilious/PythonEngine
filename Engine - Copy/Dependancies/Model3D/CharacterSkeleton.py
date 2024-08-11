"""
Copyright (C) 2023 Excilious

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


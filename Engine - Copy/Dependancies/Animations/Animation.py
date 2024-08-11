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

class Animation:
    def __init__(self):
        self.CurrentAnimations = {}

    def Create(self,AnimationListData,ID):
        self.CurrentAnimations[ID] = {}
        self.CurrentAnimations[ID]["SubsectionData"] = AnimationListData
        self.CurrentAnimations[ID]["Play"] = False
        self.CurrentAnimations[ID]["ForceHalt"] = False

    def Play(self,Subsection,ID,Object):
        if (not self.CurrentAnimations[ID]): return
        if (self.CurrentAnimations[ID]["Play"]): return

        self.CurrentAnimations[ID]["Play"] = True
        for Index,Keyframe in enumerate(Subsection.keys()):
            Object.Position = Subsection[Keyframe]
            if (self.CurrentAnimations[ID]["ForceHalt"]): 
                self.CurrentAnimations[ID]["ForceHalt"] = True 
                break

            if (Index == len(Subsection.keys())-1):
                self.CurrentAnimations[ID]["Play"] = False

    def Stop(self,Subsection,ID):
        if (not self.CurrentAnimations[ID]): return
        if (not self.CurrentAnimations[ID]["Play"]): return 

        self.CurrentAnimations[ID]["Play"] = False
        self.CurrentAnimations[ID]["ForceHalt"] = True

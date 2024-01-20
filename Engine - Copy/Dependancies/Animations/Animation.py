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
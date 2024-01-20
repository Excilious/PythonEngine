from ConfigurationsBinder import *

class Sound:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(MAXSOUNDCHANNELS)
        
        self.Channel = 0
        self.CurrentPath = SOUNDPATH

        self.AssignedSounds = {
            Sound.SQUIDWARD: self.Load('Squidward.ogg',Volume=0.2) 
        }

    def Load(self,FileName,Volume=0.5):
        NewSound = pygame.mixer.Sound(self.CurrentPath+FileName)
        NewSound.set_volume(Volume)
        NewSound.fadeout(0.5)
        return Sound
    
    def Fade(self,SoundObject,Time=0.5):
        SoundObject.fadeout(0.5)
        return SoundObject
    
    def Play(self,Sound):
        pygame.mixer.Channel(self.Channel).play(Sound)
        self.Channel += 1
    
        if (self.Channel == MAXSOUNDCHANNELS):
            self.Channel = 0
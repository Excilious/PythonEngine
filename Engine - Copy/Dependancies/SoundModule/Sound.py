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

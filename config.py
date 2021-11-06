import datetime

class config:
    """Store current state for clock radio"""

    def __init__(self):
        self.alarmTime = datetime.time
        self.radioPlaying = False
        self.volume = 50
        
    def setPlayState(self,state):
        self.radioPlaying = state

    def getPlayState(self):
        return self.radioPlaying

    def setVolume(self,volume):
        self.volume = volume

    def getVolume(self):
        return self.volume
        
    

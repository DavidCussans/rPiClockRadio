import datetime

class config:
    """Store current state for clock radio"""

    def __init__(self):

        self.alarmTime = datetime.time
        
        self.radioPlaying = False


    def setPlayState(self,state):
        self.radioPlaying = state

    def getPlayState(self):
        return self.radioPlaying
    

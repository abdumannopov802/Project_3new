class Time:
    def __init__(self, hours, minuts, secunds, msecunds) -> None:
        self.hours = hours
        self.minuts = minuts
        self.secunds = secunds
        self.msecunds = msecunds
    
    @property
    def vaqt(self):
        return f"{self.hours}:{self.minuts}:{self.secunds}:{self.msecunds}"
    
    def __str__(self) -> str:
        return self.vaqt
    
    def toString(self):
        return self.vaqt
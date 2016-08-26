class Tracked:
# This class defines the tracked object, and allowed tracking objects

    def __init__(self,mobile):
        self.mobile=mobile
        self.EnableTracking =False
        self.AllowedTrackers =[]
        self.PauseTracking =False
        self.CustomTag ={}
        self.UpdateMyLocationInterval = 300

    def __repr__(self):
        return self.mobile

    def Allow(self,track):
        if track not in self.AllowedTrackers:
            self.AllowedTrackers.append(track)
    def Revoke(self,track):
        if track in self.AllowedTrackers:
            self.AllowedTrackers.remove(track)
    def Pause(self):
        self.PauseTracking =True
class Fleet (Tracked):
    pass

class Child (Tracked):
    pass


class SchoolBus (Tracked):
    pass

class Employee (Tracked):
    pass

class lightSwitch:
    def __init__(self) :
        self.switchIsOn = False

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False


    def show(self):
        print(self.switchIsOn)
        print()     


sittingroom = lightSwitch()
sittingroom.show()
sittingroom.turnOn()
sittingroom.show()  


dinningroom = lightSwitch()
dinningroom.show()
dinningroom.turnOff()
dinningroom.show()
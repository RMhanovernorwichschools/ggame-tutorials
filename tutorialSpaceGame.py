from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import radians, sin, cos

class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        #above is object generation. This is now for the steps, which generate updated images
        self.vx = 1
        self.vy = 1
        self.vr = 0.0
        self.lturn=0
        self.rturn=0
        self.velo=0
        self.back=0
        self.fxcenter = self.fycenter = 0.5 #important for natural-looking top-down turning
        #Now this is for the animations, changing the frames in response to a button prompt (space)
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "w", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "w", self.thrustOff)
        SpaceGame.listenKeyEvent("keydown", "s", self.backupOn)
        SpaceGame.listenKeyEvent("keyup", "s", self.backupOff)
        #For question 1, let's add some turning
        SpaceGame.listenKeyEvent("keydown", "a", self.turnleft)
        SpaceGame.listenKeyEvent("keydown", "d", self.turnright)
        SpaceGame.listenKeyEvent("keyup", "a", self.noturnleft)
        SpaceGame.listenKeyEvent("keyup", "d", self.noturnright)
        
        
    def step(self): #'self' is important here because it means step happens for each individual ship
        if self.rturn==1:
            self.rotation-=0.04
        if self.lturn==1:
            self.rotation+=0.04
        self.vx=-self.velo*sin(self.rotation)
        self.vy=-self.velo*cos(self.rotation)
        self.x += self.vx
        self.y += self.vy
        if self.back==1:
            self.velo-=0.04
        # manage thrust animation
        if self.thrust == 1:
            self.velo+=0.06
            self.setImage(self.thrustframe) #self.thrustframe is just a variable (thrustframe) set below
            self.thrustframe += 1
            if self.thrustframe == 4:       #'self' is involved in this variable so its just applied to one ship
                self.thrustframe = 1
        else:
            self.setImage(0)
            self.velo=(self.velo*19)/20
    
    def thrustOn(self, event): #unsure why 'event' is important, but 'self' exists b/c each objects has its own thrust
        self.thrust = 1
    #Got it. Event is because it's called by a .listenKeyEvent
    def thrustOff(self, event):
        self.thrust = 0
    
    def turnleft(self, event):
        self.lturn =1
    
    def turnright(self, event):
        self.rturn =1
    
    def noturnleft(self, event):
        self.lturn =0
        
    def noturnright(self, event):
        self.rturn =0
    
    def backupOn(self, event):
        self.back=1
    def backupOff(self, event):
        self.back=0

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()

myapp = SpaceGame()
myapp.run()

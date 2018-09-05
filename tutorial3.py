from ggame import App, RectangleAsset, ImageAsset, SoundAsset, CircleAsset
from ggame import LineStyle, Color, Sprite, Sound

myapp = App()

# define colors and line style
green = Color(0x00ff00, 0.1)
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
ball_asset = CircleAsset(20)
ball = Sprite(ball_asset, (0, 0))
# Original image is too big. Scale it to 1/10 its original size
# custom attributes
ball.direction = 1
ball.go = True

# reverse - change the ball direction
def reverse(b):
    pop.play
    b.direction *= -1
    
# Set up function for handling screen refresh
def step():
    if ball.go:
        ball.x += ball.direction
        if ball.x + ball.width > myapp.width or ball.x < 0:
            ball.x -= ball.direction
            reverse(ball)
            print('Bounce!')
            
# Handle the space key
def spaceKey(event):
    ball.go = not ball.go

# Handle the "reverse" key
def reverseKey(event):
    reverse(ball)

# Handle the mouse click
def mouseClick(event):
    pew1.play
    ball.x = event.x
    ball.y = event.y
    
# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)

# Sounds
pew1_asset = SoundAsset("sounds/pew1.mp3")
pew1 = Sound(pew1_asset)
pop_asset = SoundAsset("sounds/reappear.mp3")
pop = Sound(pop_asset)

myapp.run(step)

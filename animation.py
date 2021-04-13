import pyglet
from pyglet.window import key

# create a window
window = pyglet.window.Window()

# load the spritesheet
image = pyglet.image.load('resources/LPC_Sara/SaraFullSheet.png')

# create an image grid (using 21 rows and and 13 columns)
image_grid = pyglet.image.ImageGrid(image, 21, 13)

# set up the walking animations, they are the 9th, 10th, 11th and 12th row
# from the bottom and set 0.1 seconds for each animation cycle
walk_up = pyglet.image.Animation.from_image_sequence(image_grid[12 * 13 : 12 * 13 + 9], 0.1)
walk_left = pyglet.image.Animation.from_image_sequence(image_grid[11 * 13 : 11 * 13 + 9], 0.1)
walk_down = pyglet.image.Animation.from_image_sequence(image_grid[10 * 13 : 10 * 13 + 9], 0.1)
walk_right = pyglet.image.Animation.from_image_sequence(image_grid[9 * 13 : 9 * 13 + 9], 0.1)

# use the first image of each cycle as "idle" animation
idle_up = image_grid[12 * 13]
idle_left = image_grid[11 * 13]
idle_down = image_grid[10 * 13]
idle_right = image_grid[9 * 13]

# create a sprite to interact with and draw
# set it to the middle of the screen
sprite = pyglet.sprite.Sprite(idle_right, window.width / 2, window.height / 2)


def on_draw():
    window.clear()
    sprite.draw()

# set up the key-press event: when the LEFT, RIGHT, TOP, UP or DOWN keys
# are pressed, exchange the sprites animation to the according walking
# animation.


def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        sprite.image = walk_up
    elif symbol == key.DOWN:
        sprite.image = walk_down
    elif symbol == key.LEFT:
        sprite.image = walk_left
    elif symbol == key.RIGHT:
        sprite.image = walk_right


# set up the key-release event: either of the arrow keys is released,
# set the sprites image to the "idle" animation of that direction

def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        sprite.image = idle_up
    elif symbol == key.DOWN:
        sprite.image = idle_down
    elif symbol == key.LEFT:
        sprite.image = idle_left
    elif symbol == key.RIGHT:
        sprite.image = idle_right


window.push_handlers(
    on_draw=on_draw,
    on_key_press=on_key_press,
    on_key_release=on_key_release,
)



# set up the movement logic. We set the movement speed to 30 pixels/second

WALK_SPEED = 30


# every tick (60th of a second) we move the sprite to the according direction.
# We multiply by `dt` (delta-time, i.e how much time has passed) to smooth out
# the movement

def tick(t):
    if sprite.image == walk_up:
        sprite.y = sprite.y + (WALK_SPEED * t)
    elif sprite.image == walk_down:
        sprite.y = sprite.y - (WALK_SPEED * t)
    elif sprite.image == walk_left:
        sprite.x = sprite.x - (WALK_SPEED * t)
    elif sprite.image == walk_right:
        sprite.x = sprite.x + (WALK_SPEED * t)

# we schedule the interval here

pyglet.clock.schedule_interval(tick, 1/60)


# finally start the application

pyglet.app.run()

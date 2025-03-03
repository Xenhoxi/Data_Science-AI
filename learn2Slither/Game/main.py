from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.orange, scale=(2.1,2.1,1))
# cube2 = Entity(model='cube', color=color.orange, scale=(1,1,1))

def update():
    cube.rotation_y += 1  # Rotate cube

app.run()


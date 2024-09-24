import py5

x, y = 0, 0
x_speed, y_speed = 2, 2
logo = None

def setup():
    global logo, x, y
    py5.size(800, 600) 
    logo = py5.load_image('/mnt/data/image.png') 
    x = py5.width / 2  
    y = py5.height / 2

def draw():
    global x, y, x_speed, y_speed
    py5.background(0) 

   
    py5.image(logo, x, y)

 
    x += x_speed
    y += y_speed

    
    if x <= 0 or x + logo.width >= py5.width:
        x_speed *= -1
    if y <= 0 or y + logo.height >= py5.height:
        y_speed *= -1

def key_pressed():
    global x_speed, y_speed
  
    if py5.key == py5.UP:
        x_speed += 1
        y_speed += 1
    elif py5.key == py5.DOWN:
        x_speed -= 1
        y_speed -= 1

py5.run_sketch()
import cv2
from PIL import ImageDraw , Image
canvas = Image.new("RGB",(512,512),"White")
draw = ImageDraw.Draw(canvas)
Prev_x = None
Prev_y = None
Prev_colour = None
for i in range(1,98):
    img = cv2.imread(r"C:\Users\tatip\Downloads\Operation-Pixel-Merge-main\Operation-Pixel-Merge-main\assets\Layer "+str(i)+".png")
    if img is None:
        continue
    height = img.shape[0]
    width = img.shape[1]
    dot_x = None
    dot_y = None
    dot_colour = None
    for y in range (height):
        for x in range(width):
            pixels = img[y,x]
            b = pixels[0]
            g = pixels[1]
            r = pixels[2]
            if b < 250 or g < 250 or r < 250:
                dot_x = x
                dot_y = y
                dot_colour = (r,g,b)
                break
        if dot_x is not None:
            break
    if dot_x == None:
        Prev_x = None
        Prev_y = None
        Prev_colour = None
    else:
        if Prev_x is not None:
            draw.line([(Prev_x,Prev_y),(dot_x,dot_y)],fill=Prev_colour,width=5)
        Prev_x = dot_x
        Prev_y = dot_y
        Prev_colour = dot_colour
canvas.save("Amfoss.png")
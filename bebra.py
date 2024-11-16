from tkinter import *
from PIL import Image, ImageTk

size = 3
width = 1360
height = 768
p_width = 640
p_height = 360
x_offset = 0
y_offset = 0
x_velocity = 1
y_velocity = 1

root = Tk()
root.title("Waiting screen")
root.geometry(str(width) + "x" + str(height))
root.attributes('-fullscreen', True)
c = Canvas(width=width, height=height, bg="black", borderwidth=0, highlightthickness=0)
c.pack()

image = Image.open("C:/Users/pablo/Pictures/Экран/photo1711737358.jpeg")
image = image.resize((p_width, p_height))
photo = ImageTk.PhotoImage(image)
ball = c.create_image(0, 0, image=photo)
#ball = c.create_rectangle(0, 0, 50, 50, fill="blue")
#text = c.create_text(25, 25, text="бебра", font=('Courier', 18))

xvec = 0
yvec = 0
xi = 1
yi = 1
x = x_offset
y = y_offset
x1 = x_offset + p_width
y1 = y_offset + p_height

def animate():
    global xvec
    global yvec
    global xi
    global yi
    global x
    global y
    global x1
    global y1
    xvec += x_velocity * xi
    yvec += y_velocity * yi
    c.coords(ball, (x+x1)/2+xvec,(y+y1)/2+yvec)
    #c.coords(ball, x+xvec, y+yvec, x1+xvec, y1+yvec)
    #c.coords(text, (x+x1)/2+xvec, (y+y1)/2+yvec)
    c.after(10, animate)
    if(x1+xvec > width or x+xvec < 0):
        xi *= -1
    if(y1+yvec > height or y+yvec < 0):
        yi *= -1

animate()

root.mainloop()

from PIL import Image

im = Image.open("img1.jpeg")
print(im.size)

# new_size = im.resize((500,500))
# new_size.show()

# new_height = 720
# new_width =  new_height / im.height * im.width
# print(new_width)

# new_size = im.resize((new_height, int(new_width)))
# new_size.show()


# Manually Fined Tuned Values
# x1 = 0
# y1 = 0
# x2 = im.width * (0.75)
# y2 = im.height * (0.75)
# cropped = im.crop((x1 + im.width * (0.25), y1 + im.height * (0.25), x2 -100, y2 -100))
# cropped.show()

# Equal space crop
xcenter = im.width/2
ycenter = im.height/2
kfactor = 200
x1 = xcenter - kfactor
y1 = ycenter - kfactor
x2 = xcenter + kfactor
y2 = ycenter + kfactor
cropped = im.crop((x1, y1, x2, y2))
cropped.show()

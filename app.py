#Task 5

from PIL import Image, ImageFilter

im = Image.open("Butterfly.jpg")

blured_im = im.filter(ImageFilter.BLUR)
im_1 = im.convert("1")
im_L = im.convert("L")
im_LA = im.convert("LA")

blured_im.show()
im_1.show()
im_L.show()
im_LA.show()

blured_im.save("blured.png")
im_1.save("im_1.png")
im_L.save("im_L.png")
im_LA.save("im_LA.png")

# Task 7

(width, height) = im_1.size
data = list(im_1.getdata())

f = open(r"C:/Users/yanba/Documents/GitHub/python-lab-1/ph2.txt", "w")
count = 0

print(type(data))
print((width, height))
for i in data:
    if i == 255:
        f.write("11")
    if i == 0:
        f.write("00")
    count += 1
    if count == width:
        count = 0
        f.write("\n")

f.close()

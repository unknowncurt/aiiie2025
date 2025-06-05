from PIL import Image

print('PIL', Image.__version__)

my_image = Image.open("cat_1749017411.jpg")

for x in range(my_image.width):
  for y in range(my_image.height):
    if x % 2 == 0 :
      my_image.putpixel((x,y), (24,211,68))
    
my_image.show()

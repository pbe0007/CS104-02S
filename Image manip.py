from PIL import Image
import random
image_file = "uah_logo_rgb.png"
img_logo = Image.open(image_file)
width, height = img_logo.size
# const_color = "#FFFFFF"
#def color_key(color):
#    color_R = int("0x" + color.removeprefix("#")[:2],16)
#    color_G = int("0x" + color.removeprefix("#")[2:4],16)
#    color_B = int("0x" + color.removeprefix("#")[4:],16)
#    return (color_R,color_G,color_B)
display(img_logo)
### img = Image.new("RGB", (width,height), color)
pixels = img_logo.load()
seed = 173
for x in range(width):
    for y in range(height):
        key = random.randint(0,255)      # color_key(str(hex(random.randint(0,16777215)))[2:])
        pixel = pixels[x,y]
        new_R = pixel[0] ^ key #[0]
        new_G = pixel[1] ^ key #[1]
        new_B = pixel[2] ^ key #[2]
        pixels[x,y] = (new_R,new_G,new_B)
        #print(pixels[x,y])
        #break
    #break
#display(img_logo)

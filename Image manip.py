from PIL import Image
import random
import sys
image_file = sys.argv[1]
img_logo = Image.open(image_file)
width, height = img_logo.size
print(__name__)

def image_encrypt(image_file, seed):
    random.seed(seed)
    pixels = image_file.load()
    for x in range(width):
        for y in range(height):
            key = random.randint(0,255)
            pixel = pixels[x,y]
            new_R = pixel[0] ^ key #[0]
            new_G = pixel[1] ^ key #[1]
            new_B = pixel[2] ^ key #[2]
            pixels[x,y] = (new_R,new_G,new_B)
    return image_file

if __name__ == "__main__":
    encrypted = image_encrypt(Image.open(image_file), sys.argv[2])
    encrypted.show()

    decrypted = image_encrypt(encrypted, sys.argv[2])
    decrypted.show()

            #print(pixels[x,y])
            #break
        #break
    #display(img_logo)
    img_logo.save("new_image.png")
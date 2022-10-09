from PIL import Image
from assets.leonResources import banner
ascii_char=["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]
banner.leonBanner()
# image path
image_path="./Images/backdoor-removebg-preview(1).png"
try:
    image=Image.open(image_path)
except Exception as e:
    print(e)

# resize the Image
width,height=image.size
aspectRatio=height/width
new_width=50
new_height=aspectRatio*new_width
image=image.resize((new_width,int(new_height)))

# convert image to grey scale
image=image.convert('L')

# take the image pixels
pixels=image.getdata()
ascii_str=""
for pixel in pixels:
    ascii_str+=ascii_char[pixel//25]
print(ascii_str)

img_width = new_width
ascii_str_len = len(ascii_str)
ascii_img=""
#Split the string based on width  of the image
for i in range(0, ascii_str_len, img_width):
    ascii_img += ascii_str[i:i+img_width] + "\n"
#save the string to a file
with open("ascii_image.txt", "w") as f:
    f.write(ascii_img);
    
    


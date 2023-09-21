# Created by John Herbert 20 Sep 2023
# MIT License
# Draw color blocks for a palette
# 176 colors in the palette with a black block appearing at the start of each row (187 blocks total)

from PIL import Image

# Define the size of the palette image
# Calculate the width of each color block
block_width = 64
block_height = 64
offset = 17
total_rows = 11
# Calculate the width of each color block
width, height = block_width * offset, block_height * total_rows


# Create a new blank image with a white background
palette_image = Image.new("RGB", (width, height), "white")

# Define a list of colors for your palette

red = []
pink = []
purple = []
orange = []
yellow = []
green = []
cyan = []
blue = []
brown = []
gray = []
tan = []

# step through the color value adding 16 each time
for i in [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]:
    color = (i, 0, 0)
    red.append(color)
    color = (i-92, i-128, i-16)
    purple.append(color)
    color = (i, i-92, 0)
    orange.append(color)
    color = (i, i, 0)
    yellow.append(color)
    color = (0, i, 0)
    green.append(color)
    color = (0, i, i)
    cyan.append(color)
    color = (0, 0, i)
    blue.append(color)
    color = (i-64, i-128, i-192)
    brown.append(color)
    color = (i-16, i-64, i-128)
    tan.append(color)
    color = (i, i, i)
    gray.append(color)
    color = (i-32, i-116, i-128)
    pink.append(color)


# Draw the color blocks on the palette
for x in range(0, offset):
        color_look_up_value = x
        palette_image.paste(red[color_look_up_value], (x*block_width, 0, (x+1) * block_width, block_height))
        palette_image.paste(pink[color_look_up_value], (x*block_width, block_height, (x+1) * block_width, block_height*2))
        palette_image.paste(orange[color_look_up_value], (x*block_width, block_height*2, (x+1) * block_width, block_height*3))
        palette_image.paste(yellow[color_look_up_value], (x*block_width, block_height*3, (x+1) * block_width, block_height*4))
        palette_image.paste(green[color_look_up_value], (x*block_width, block_height*4, (x+1) * block_width, block_height*5))
        palette_image.paste(cyan[color_look_up_value], (x*block_width, block_height*5, (x+1) * block_width, block_height*6))
        palette_image.paste(blue[color_look_up_value], (x*block_width, block_height*6, (x+1) * block_width, block_height*7))
        palette_image.paste(purple[color_look_up_value], (x*block_width, block_height*7, (x+1) * block_width, block_height*8))
        palette_image.paste(brown[color_look_up_value], (x*block_width, block_height*8, (x+1) * block_width, block_height*9))
        palette_image.paste(tan[color_look_up_value], (x*block_width, block_height*9, (x+1) * block_width, block_height*10))
        palette_image.paste(gray[color_look_up_value], (x*block_width, block_height*10, (x+1) * block_width, block_height*11))



# Save the palette image as a PNG file
palette_image.save("color_palette.png")

# Display the palette image
palette_image.show()
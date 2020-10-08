from PIL import Image

# Open image and get pixels
image = Image.open('onehundredeightypointone.png')
pix = image.load()
width, height = image.size

# Find any pixels that are not pure white
colored_pixels = []
for x in range(width):
    for y in range(height):
        if pix[x, y] != (255, 255, 255, 255):
            colored_pixels.append((x,y))

# Find the boundary pixels
min_x = min([px[0] for px in colored_pixels])
max_x = max([px[0] for px in colored_pixels])
min_y = min([px[1] for px in colored_pixels])
max_y = max([px[1] for px in colored_pixels])

print("Minimum x: {}".format(min_x))
print("Maximum x: {}".format(max_x))
print("Minimum y: {}".format(min_y))
print("Maximum y: {}".format(max_y))

# Find the (x, y) values for all four corners

# What is upper left corner?
x = min_x
y = max([px[1] for px in colored_pixels if px[0] == x])
print("Upper left corner: ({}, {})".format(x, y))

# What is upper right corner?
x = max_x
y = max([px[1] for px in colored_pixels if px[0] == x])
print("Upper right corner: ({}, {})".format(x, y))

# What is lower left corner?
y = min_y
x = min([px[0] for px in colored_pixels if px[1] == y])
print("Lower left corner: ({}, {})".format(x, y))

# What is lower right corner?
y = min_y
x = max([px[0] for px in colored_pixels if px[1] == y])
print("Lower right corner: ({}, {})".format(x, y))
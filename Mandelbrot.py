from PIL import Image
import math, numpy
import colorsys
import matplotlib.pyplot as plt

"""
Calculates and generates an image of the mandelbrot set
"""


# image width
H = 250
# image height
W = 250
# iteration limit
n = 255

# drawing area
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5

# the complex function that we repeatedly apply
f = lambda c, z: z ** 2 + c

# calculates the magnitude of a complex number
def mag(c):
    x = c.real
    y = c.imag
    mag = x * x + y * y
    return math.sqrt(mag)

# repeatedly applies f until the iteration limit is reach or mag goes over 2
def mandel(c, n):
    z = (0 + 0j)
    for i in range(n):
        z = f(c, z)
        if mag(z) >= 2:
            return i + 1
    return i + 1

# creates a blank image
img = Image.new('RGB', (W, H))
pixels = img.load()

# checks every pixel in the image to see if it is inside or outside the set
for x in range(W):
    cx = x * (xb - xa) / (W - 1) + xa
    # displaying the progress as percentage
    if (x%10)==0:
        print("%.2f %%" % (x / W * 100.0))

    for y in range(H):
        cy = y * (yb - ya) / (H - 1) + ya
        c = cx + cy * 1j

        i = mandel(c, n)
        img.putpixel((x, y), (i,i%2,i%4,100))

# displays the image
plt.imshow(img)
plt.show()
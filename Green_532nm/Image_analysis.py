# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:23:25 2021

@author: jiju4
"""

from PIL import Image, ImageChops
from matplotlib import pyplot as plt

i1 = Image.open("X:\Sem 5\Project\Images\Jiju\Jiju_air\HH.tiff") 
i2 = Image.open("X:\Sem 5\Project\Images\Jiju\Jiju_air\VV.tiff")

assert i1.mode == i2.mode, "Different kinds of images."
assert i1.size == i2.size, "Different sizes."
 
pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
ncomponents = i1.size[0] * i1.size[1] * 3
print ("Difference (percentage):", (dif / 255.0 * 100) / ncomponents)
diff = ImageChops.difference(i1,i2)

print ("size of the image1", i1.size)
print ("size of the image2", i2.size)
#for ploting the images compared
plt.subplot(121), plt.imshow(i1)
plt.axis("off")
plt.subplot(122), plt.imshow(i2)
plt.axis("off")
# to show the difference of both images
if diff.getbbox():
    diff.show()
    
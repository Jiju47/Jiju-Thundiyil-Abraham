# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:21:45 2021

@author: jiju4
"""
from PIL import ImageChops, Image, ImageStat
import matplotlib.pyplot as plt 
import numpy as np
actual_error = 0
im1 = Image.open("X:\Sem 5\Project\Images\Jiju\Jiju_air\HH.tiff")
#Passing the image 1 to the stat function of the imagestat class
stat1  = ImageStat.Stat(im1)
print(stat1.rms ,"Root mean Square of image 1")
print(stat1.mean ,"Mean of image 1")
#rms is root mean square of all pixels for each band in an image  mean is Mean of all pixels for each band in an image
x = np.array(im1.histogram())

im2 = Image.open("X:\Sem 5\Project\Images\Jiju\Jiju_air\HR.tiff")
#Passing the image2 to the stat function of the imagestat class
stat2  = ImageStat.Stat(im2)
print(stat2.rms , "Root mean Square of image 2" )
print(stat2.mean ,"Mean of image 2")

y = np.array(im2.histogram())
# Size of both the images
width1, height1 = im1.size
print ("size of the image1:", im1.size, "Total pixels:", width1 * height1)
width2, height2 = im2.size
print ("size of the image2", im2.size, "Total pixels:", width2 * height2) 

try:
    if len(x) == len(y):
        error = np.sqrt(((x - y) ** 2).mean())
        error = str(error)[:2]
        actual_error = float(100) - float(error)
#Difference of both the images
    diff = ImageChops.difference(im1, im2).getbbox()

    if diff:
        print("Not Duplicate Image")
        print('Matching Images In percentage: ', actual_error,'\t%' )
        f = plt.figure()
        text_lable = str("Matching Images Percentage" + str(actual_error)+"%")
        print("Difference in Images by percentange", 100 - actual_error,"\t%")
#Plotting the image1     
        plt.suptitle(text_lable)
        f.add_subplot(1,2, 1)
        plt.imshow(im1)
        f.add_subplot(1,2, 2)
        plt.imshow(im2)
        plt.show(block=True)
    else:
        print("Duplicate Image")
        print('Matching Images In percentage: ', actual_error,'%' )
        f = plt.figure()
        text_lable = str("Matching Images Percentage" + str(actual_error)+"%")
        print("Difference in Images in percentange", 100 - actual_error,"\t%")
#Plotting the image2        
        plt.suptitle(text_lable)
        f.add_subplot(1,2, 1)
        plt.imshow(im1)
        f.add_subplot(1,2, 2)
        plt.imshow(im2)
        plt.show(block=True)
        
except ValueError as identifier:
    f = plt.figure()
    text_lable = str("Matching Images Percentage " + str(actual_error)+"%")
    plt.suptitle(text_lable)
    f.add_subplot(1,2, 1)
    plt.imshow(im1)
    f.add_subplot(1,2, 2)
    plt.imshow(im2)
    plt.show(block=True)
    print('identifier: ', identifier)


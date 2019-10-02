# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:08:24 2019

@author: pnbal
"""

import cv2, os

print("Listing all images in the current directory.")
ext = [".jpg",".jpeg"]
for file in os.listdir('./'):
    if file.endswith(tuple(ext)):
        print(file)
imgname = input("Enter the name of the image: ")
img=cv2.imread(imgname)
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
print("Saving the B/W image with name enh_%s in the current directory"%(imgname))
if not cv2.imwrite("enh_%s"%(imgname), enh_img):
    raise Exception("Failed")
print("Done!")
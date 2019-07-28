# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:08:24 2019

@author: pnbal
"""

import cv2 

img=cv2.imread('IMG_20190709_194910.jpg')
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
cv2.imwrite('ech.png',enh_img)
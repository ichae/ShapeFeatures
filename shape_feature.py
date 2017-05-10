# -*- coding: utf-8 -*-
"""
ShapeFeature.py
Created on Wed May 10 08:53:02 2017

@author: Cho
"""
import cv2
import numpy as np
from skimage.measure import label, regionprops

im = cv2.imread('img4.jpg', 0)
_, bw = cv2.threshold(im, 125, 255, cv2.THRESH_BINARY_INV)

Lnum, Limg = cv2.connectedComponents(bw)

_, contours, _ = cv2.findContours(bw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

# Area
area = cv2.contourArea(cnt)

# Perimeter
perimeter = cv2.arcLength(cnt, True)

# solidity
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

# Extent
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

# Aspect Ratio
_, (maxD,minD), _ = cv2.minAreaRect(cnt)
AspRatio = minD/maxD 

# compactness1,2 & Elongation
eqD = np.sqrt(4 *area / 3.14)
comp1 = eqD/maxD
comp2 = minD/eqD
Elong = (maxD-minD)/maxD

# Cicularity
cir = 4*3.14*area/perimeter**2
    

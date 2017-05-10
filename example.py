# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:49:15 2017

@author: Cho
"""

import cv2
import numpy as np
import regionprops as rg

im = cv2.imread('img1.jpg', 0)
_, bw = cv2.threshold(im, 125, 255, cv2.THRESH_BINARY_INV)

_, contours, _ = cv2.findContours(bw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

a = rg._RegionProperties(cnt)
B = rg.regionprops(contours)
C = rg.regionpropsAll(contours)

print(a.area)
print(a.perimeter)
print(a.solidity())
print(B[0].area)
print(C)
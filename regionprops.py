# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:53:47 2017

@author: Cho
"""
import cv2
import numpy as np

class _RegionProperties(object):
	def __init__(self, cnt):
		self.cnt = cnt
		self.area = cv2.contourArea(self.cnt)
		self.perimeter = cv2.arcLength(self.cnt, True)
		_, (self.maxD, self.minD), _ = cv2.minAreaRect(self.cnt)

	def solidity(self):
		self.hull = cv2.convexHull(self.cnt)
		self.hull_area = cv2.contourArea(self.hull)
		return float(self.area)/self.hull_area	

	def Extent(self):
		x,y,w,h = cv2.boundingRect(self.cnt)
		rect_area = w*h
		return float(self.area)/rect_area
	
	def AspRatio(self):
		return self.minD/self.maxD

	def compactness(self):
		self.eqD = np.sqrt(4 *self.area / 3.14)
		comp1 = self.eqD/self.maxD
		comp2 = self.minD/self.eqD
		return(comp1, comp2)

	def ELong(self):
		return (self.maxD-self.minD)/self.maxD

	def circularity(self):
		return 4*3.14*self.area/self.perimeter**2

def regionprops(contours):
    """
    area, perimeter, solidity, Extent, AspRatio, compactness, ELong, circularity \n
    -----------------\n
    im = cv2.imread('img.jpg', 0) \n    
    _, bw = cv2.threshold(im, 125, 255, cv2.THRESH_BINARY_INV) \n     
    _, contours, _ = cv2.findContours(bw, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)  \n   
    cnt = contours[0]    \n 
    B = rg.regionprops(contours)    \n 
    B[0].area \n 
    """
    regions = []
    for cnt in contours:
        props = _RegionProperties(cnt)
        regions.append(props)
    return regions

def regionpropsAll(contours):
    """
    area, perimeter, solidity, Extent, AspRatio, compactness1, compactness2, ELong, circularity
    """
    regions = []
    for cnt in contours:
        props = _RegionProperties(cnt)
        pr = [props.area, props.perimeter, props.circularity(), props.solidity(), props.Extent(), props.AspRatio(), props.compactness()[0], props.compactness()[1], props.ELong(), props.circularity()]
        regions.append(pr)
    return regions







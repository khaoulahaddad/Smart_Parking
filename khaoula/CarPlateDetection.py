#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import imutils
import pytesseract
import argparse
import re
import sqlite3 as sql
# Read the image file

#image = cv2.imread('/home/khaoula/Desktop/Smart_Parking/matricule2.jpg')
image=cv2.imread('/home/khaoula/Desktop/Smart_Parking/matricule.jpg')

# Resize the image - change width to 500

image = imutils.resize(image, width=500)

# Display the original image
#cv2.imshow("Original Image", image)

# RGB to Gray scale conversion

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

##cv2.imshow("1 - Grayscale Conversion", gray)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)

gray = cv2.bilateralFilter(gray, 11, 17, 17)

##cv2.imshow("2 - Bilateral Filter", gray)

# Find Edges of the grayscale image

edged = cv2.Canny(gray, 300, 100)

#cv2.imshow("4 - Canny Edges", edged)

# Find contours based on Edges

(new, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                                  cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]  # sort contours based on their area keeping minimum required area as '30' (anything smaller than this will not be considered)
NumberPlateCnt = None  # we currently have no Number plate contour

# loop over our contours to find the best possible approximate contour of number plate

count = 0
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.07 * peri, True)
    #cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
    #print(len(approx))
    if len(approx) == 4:  # Select the contour with 4 corners
        NumberPlateCnt = approx  # This is our approx Number Plate Contour

        break

# Drawing the selected contour on the original image

cv2.drawContours(image, [NumberPlateCnt], -1, (0, 255, 0), 3)
cv2.imshow('Final Image With Number Plate Detected', image)
# Masking the part other than the number plate2
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1,)
new_image = cv2.bitwise_and(image,image,mask=mask)

# Now crop
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]
#cv2.imshow('edged',Cropped)
mask = np.zeros(Cropped.shape,np.uint8)

#cv2.rectangle(Cropped , (100,0) ,(163,30),(255, 0, 0), 2)
#cv2.rectangle(Cropped, (0,0) ,(50,30),(255, 0, 0), 2)

#cv2.rectangle(Cropped, (50,0), (100, 30), (255, 0, 0), -1) 
#cv2.imwrite("detection3.png", Cropped)
#Read the number plate
text = pytesseract.image_to_string(Cropped,lang='eng',config = "--oem 3 --psm 6", nice=0)
print(text)
res=[int(s) for s in text.split() if s.isdigit()]
resultat_gauche=str(res[0])
resultat_droite=str(res[len(res)-1])
if (len(resultat_droite)>4):
        text=''
        for i in range((len(resultat_droite)-1),(len(resultat_droite)-5) , -1):
                text=resultat_droite[i] + text
        resultat_droite = text
#liste=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#for i in range(0,4):
#        if(text[i] in liste):
#                resultat_gauche=resultat_gauche+ text[i]
#for i in range((len(text)-1),(len(text)-5) , -1):
#        if(text[i] in liste):
#                resultat_droite=text[i]+ resultat_droite
print(resultat_gauche)
print(resultat_droite)

        
db=sql.connect("/home/khaoula/Desktop/Smart_Parking/khaoula/db.db")
cursor=db.cursor()
cursor.execute("""INSERT INTO khaoulaApp_test (matricule_gauche , matricule_droite) VALUES(?, ?)""", (int(resultat_gauche),resultat_droite))
db.commit()

#cv2.imshow('image',image)
#cv2.imshow('Cropped',Cropped)
cv2.waitKey(0)  # Wait for user input before closing the images displayed

			

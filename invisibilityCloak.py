import cv2
import numpy as np
from caliberation import Caliberation,Tranform

vc = cv2.VideoCapture(0) #uses the primary camera(web-cam)

#Step 1: Capture background image

print('Press any key once suitable background image has been obtained: ')
while cv2.waitKey(1) == -1:
    return_value, frame = vc.read()
    frame = cv2.flip(frame, 1)  #to avoid lateral inversion
    frame = cv2.resize(frame, (1280,760))
    cv2.imshow('frame',frame)
cv2.imwrite('background.png',frame)
cv2.destroyAllWindows()
print('\n\n\tBackground image has been captured!!!')

#Step 2: HSV Color Range for cloak

c = input('Press Enter to start Caliberation: ')
Lower,Upper = Caliberation()
print(Lower,Upper)

#Step 3: Real time application
c = input('Press enter to start Magiccccc!!! ')
vc.release()
background = cv2.imread('background.png')
vc = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:
    return_value, frame = vc.read()
    frame = np.flip(frame, 1)
    frame = cv2.resize(frame, (1280,760))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(Lower), np.array(Upper))
    mask = Tranform(mask)
    cv2.imshow('Caliberate',mask)

    frame = np.array(frame)
    temp = cv2.bitwise_and(background,background,mask = mask)
    mask = cv2.bitwise_not(mask)
    frame = cv2.bitwise_and(frame,frame,mask = mask)
    frame = cv2.add(frame,temp)
    cv2.imshow('Frame',frame)


vc.release()
cv2.destroyAllWindows()

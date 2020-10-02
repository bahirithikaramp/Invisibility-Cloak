import cv2
import numpy as np

def Tranform(mask):
    cv2.imshow('Mask',mask)
    kernel = np.ones((10,10),np.uint8)
    mask = cv2.erode(mask,kernel,iterations = 5)
    mask = cv2.dilate(mask,kernel,iterations = 8)
    return mask

def Empty(x):
    pass

def Caliberation():
    vc = cv2.VideoCapture(0)
    cv2.namedWindow('Caliberate HSV')
    cv2.createTrackbar('L_HUE','Caliberate HSV',0,179,Empty)
    cv2.createTrackbar('L_SAT','Caliberate HSV',0,255,Empty)
    cv2.createTrackbar('L_VAL','Caliberate HSV',0,255,Empty)
    cv2.createTrackbar('U_HUE','Caliberate HSV',0,179,Empty)
    cv2.createTrackbar('U_SAT','Caliberate HSV',0,255,Empty)
    cv2.createTrackbar('U_VAL','Caliberate HSV',0,255,Empty)
    cv2.setTrackbarPos('U_HUE','Caliberate HSV',179)
    cv2.setTrackbarPos('U_SAT','Caliberate HSV',255)
    cv2.setTrackbarPos('U_VAL','Caliberate HSV',255)
    while cv2.waitKey(1) == -1:
        return_value, frame = vc.read()
        frame = cv2.resize(frame, (480,480))
        frame = np.flip(frame, 1)
        cv2.imshow('Frame',frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        L_HUE = cv2.getTrackbarPos('L_HUE','Caliberate HSV')
        L_SAT = cv2.getTrackbarPos('L_SAT','Caliberate HSV')
        L_VAL = cv2.getTrackbarPos('L_VAL','Caliberate HSV')
        U_HUE = cv2.getTrackbarPos('U_HUE','Caliberate HSV')
        U_SAT = cv2.getTrackbarPos('U_SAT','Caliberate HSV')
        U_VAL = cv2.getTrackbarPos('U_VAL','Caliberate HSV')

        Lower = [L_HUE, L_SAT, L_VAL]
        Upper = [U_HUE, U_SAT, U_VAL]

        mask = cv2.inRange(hsv, np.array(Lower), np.array(Upper))
        mask = Tranform(mask)

        cv2.imshow('Caliberate',mask)

    vc.release()
    cv2.destroyAllWindows()
    return Lower, Upper

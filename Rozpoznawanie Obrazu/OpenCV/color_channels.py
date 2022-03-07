import cv2 as cv
import numpy as np
camera = cv.VideoCapture(0)
while(True):

    isTrue, frame = camera.read()
    blank = np.zeros(frame.shape[:2],dtype='uint8')

    b,g,r = cv.split(frame)
    blue = cv.merge([b,blank,blank])
    green = cv.merge([blank,g,blank])
    red = cv.merge([blank,blank,r])
    cv.imshow('frame', frame)
    cv.imshow('blue', blue)
    cv.imshow('green', green)
    cv.imshow('red', red)

    if cv.waitKey(1) == ord('q'):
        break

import cv2 as cv
import numpy as np

def get_camera_object(cameras_number=2):
    for i in range(cameras_number):
        cap =  cv.VideoCapture(i)
        if not (cap is None or not cap.isOpened() or cap.read()[1] is None):
            return cap
camera = get_camera_object()

while(True):
    isTrue, frame = camera.read()
    blank = np.zeros(frame.shape[:2],dtype='uint8') # generowanie pustej maski rozmiarów klatki
    mask = cv.circle(blank,(frame.shape[1]//2,frame.shape[0]//2),200,255,-1) # definiujecie maskę, nadając jej kształt
    mask = cv.circle(mask,(frame.shape[1]//2,frame.shape[0]//2+200),200,255,-1)
    masked = cv.bitwise_and(frame,frame,mask=mask) # operacja bitowa maski z docelowym obrazem
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('masked', masked)

    if cv.waitKey(1) == ord('q'):
        break


camera.release()

cv.destroyAllWindows()

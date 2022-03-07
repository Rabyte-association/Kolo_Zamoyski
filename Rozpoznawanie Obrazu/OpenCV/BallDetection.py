#Importing libraries
import datetime
import cv2
import numpy as np
import math
import json
import threading
from threading import Thread

cv2.useOptimized()

class FPS:
    def __init__(self):
        # store the start time, end time, and total number of frames
        # that were examined between the start and end intervals
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        # start the timer
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        # stop the timer
        self._end = datetime.datetime.now()

    def update(self):
        # increment the total number of frames examined during the
        # start and end intervals
        self._numFrames += 1

    def elapsed(self):
        # return the total number of seconds between the start and
        # end interval
        return (self._end - self._start).total_seconds()

    def fps(self):
        # compute the (approximate) frames per second
        return self._numFrames / self.elapsed()

class WebcamVideoStream:
    def __init__(self, src=0,):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        #self.stream.set(3, 1280)
        #self.stream.set(4, 720)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False
    def start(self):
    # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()


    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
def zoom(frame,scale):
    if(scale<1):
        scale=1
    height, width, channels = frame.shape

    #prepare the crop
    centerX,centerY=int(height/2),int(width/2)
    radiusX,radiusY= int(height/(scale*2)),int(width/(scale*2))

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    cropped = frame[minX:maxX, minY:maxY]
    frame = cv2.resize(cropped, (width, height))
    return frame

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

def nothing(x):
    pass
def send(distance,angle):
    angle*=angleConst
    print("Distance: {} \n Angle: {}".format(distance,angle))
    sd.putNumber("Ball distance", distance)
    sd.putNumber("Angle", angle)


cond = threading.Condition()
notified = [False]

with open('BallParameters.json', 'r') as f:
    data = json.load(f)

print(data)

#Focus constant
#Focus= 874.7983468465262
Focus=1195.754716981132

dist=135
Width=18
angleConst=0.0625


print("Which mode do you want to use?\n1.Dev \n2.User\n3.Jetson")
while True:
    choice = input("Your choice: ")
    if(choice=='1'):
        mode=1
        break
    elif(choice=='2'):
        mode=2
        break
    elif(choice=='3'):
        mode=3
        break
    else:
        print("Incorrect input!\n\n\n")


if mode==1:
    cv2.namedWindow("Color")
    cv2.createTrackbar("LH", "Color", data['Low_H'], 255, nothing)
    cv2.createTrackbar("LS", "Color", data['Low_S'], 255, nothing)
    cv2.createTrackbar("LV", "Color", data['Low_V'], 255, nothing)
    cv2.createTrackbar("UH", "Color", data['Upper_H'], 255, nothing)
    cv2.createTrackbar("US", "Color", data['Upper_S'], 255, nothing)
    cv2.createTrackbar("UV", "Color", data['Upper_V'], 255, nothing)

    cv2.namedWindow("Noise")
    cv2.createTrackbar("KernelSize", "Noise", data['KernelSize'], 20, nothing)
    cv2.createTrackbar("Iterations", "Noise", data['Iterations'], 20, nothing)
    cv2.createTrackbar("CircleDet", "Noise", data['CircleDet'], 20, nothing)
    cv2.createTrackbar("minCircle", "Noise", data['minCircle'], 100, nothing)


if mode<3:
    cv2.namedWindow("Zoom")
    cv2.createTrackbar("Scale", "Zoom", 1, 50, nothing)

if mode==3:
    NetworkTables.initialize(server='10.81.27.2')
    NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
    with cond:
        print("Waiting")
        if not notified[0]:
            cond.wait()
        sd = NetworkTables.getTable("Dashboard")
cap = WebcamVideoStream().start()
fps = FPS().start()
while True:
    try:
        #Getting values from trackbar

        frame = cap.read()

        if mode==1:
            l_h = cv2.getTrackbarPos("LH", "Color")
            l_s = cv2.getTrackbarPos("LS", "Color")
            l_v = cv2.getTrackbarPos("LV", "Color")

            u_h = cv2.getTrackbarPos("UH", "Color")
            u_s = cv2.getTrackbarPos("US", "Color")
            u_v = cv2.getTrackbarPos("UV", "Color")

            KernelSize = cv2.getTrackbarPos("KernelSize", "Noise")
            iterations = cv2.getTrackbarPos("Iterations", "Noise")
            CircleDet = cv2.getTrackbarPos("CircleDet", "Noise")
            minCircle = cv2.getTrackbarPos("minCircle", "Noise")
        else:
            l_h = data['Low_H']
            l_s = data['Low_S']
            l_v = data['Low_V']

            u_h =data['Upper_H']
            u_s = data['Upper_S']
            u_v = data['Upper_V']

            KernelSize = data['KernelSize']
            iterations = data['Iterations']
            CircleDet = data['CircleDet']
            minCircle = data['minCircle']

        if mode<3:
            scale = cv2.getTrackbarPos("Scale", "Zoom")
        if(scale>1):
            frame = zoom(frame,scale)
        #chaniging colors to hsv format
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #Setting hsv range and setting up the mask
        lower_color = np.array([l_h,l_s,l_v])
        upper_color = np.array([u_h,u_s,u_v])
        mask = cv2.inRange(hsv, lower_color, upper_color)

        #Creating result frame
        result = cv2.bitwise_and(frame, frame, mask=mask)

        #Morphological operations
        kernel = np.ones((KernelSize,KernelSize),np.uint8)
        result = cv2.erode(result,kernel,iterations = iterations)
        result = cv2.dilate(result,kernel,iterations = iterations)

        #Result to grey
        imgray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        #Detecting contours
        contours, hierarchy = cv2.findContours(imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            #Approxying contours
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)

            #Checking if circle
            if len(approx)>CircleDet:
                cv2.drawContours(result, [contour], 0, (0, 0, 255), 3)
                gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

                #Calculating moments of an image
                M = cv2.moments(contour)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                #Calculating radius of a ball on an image
                n=0
                rSum=0
                for c in contour:
                    n+=1
                    rSum+=math.sqrt((c[0][0]-cX)**2+(c[0][1]-cY)**2)
                r=rSum/n

                r=int(r)

                if(r>minCircle):
                    #Drawing circle
                    cv2.circle(frame, (cX, cY), r, (165,37, 140), 3)

                    #Calculating distance
                    distance=(Width*Focus)/(2*r)
                    distance=int(distance)
                    angle=frame.shape[1]/2-cX

                    cv2.putText(frame,"{} cm".format(distance), (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 1, (165,37, 140), 2)
                    #cv2.putText(frame,"{} px".format(angle), (cX, cY+15),cv2.FONT_HERSHEY_SIMPLEX, 1, (165,37, 140), 2)
                    if mode == 3:
                        send(distance,angle)


        #cv2.imshow("gray", thresh)
        if mode==1 or mode==2:
            dsize = (500, 300)
            frame = cv2.resize(frame, dsize)
            cv2.imshow("frame", frame)
            if mode == 1:
                result = cv2.resize(result, dsize)
                cv2.imshow("res", result)
            #Key to exit
            key = cv2.waitKey(1)
            if key == 27:
                break
            fps.update()
    except:
        print("")
        break

#Clean up
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cap.stop()
cv2.destroyAllWindows()
print("Focus: {}".format(Focus))
if mode==1:
    outputNoise={"Low_H" : l_h,"Low_S" : l_s,"Low_V" : l_v,"Upper_H" : u_h,"Upper_S" : u_s,"Upper_V" : u_v,"KernelSize": KernelSize, "Iterations" : iterations, "CircleDet" : CircleDet, "minCircle" : minCircle}
    print(outputNoise)

    decision = input("Do you want to save the changes?(Y/N): ")
    if(decision=="Y" or decision=="y"):
        noiseSettings = json.dumps(outputNoise)
        f = open("BallParameters.json","w")
        f.write(noiseSettings)
        f.close()
        print("File saved successfully!")

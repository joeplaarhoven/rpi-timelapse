import time
import picamera
import numpy as np
from PIL import Image
import datetime
import cv2
import glob


picturesMin = input("Please enter the amount of pictures per minute: \n")
lengthTimeLapse = input("Please enter the length of the timelapse in minutes: \n")
amountOfPictures = int(lengthTimeLapse) * int(picturesMin);
timeBetweenPic = 60 / int(picturesMin);
def take_frame():
    with picamera.PiCamera(resolution='512x512', framerate=24) as camera:

        # camera.resolution = (512, 512)
        # camera.framerate = 24


        output = np.empty((512 * 512 * 3,), dtype=np.uint8)
        camera.capture(output, 'rgb')
        output = output.reshape((512, 512, 3))
        output = output[:512, :512, :]
        data = output
        time.sleep(timeBetweenPic)
        return data


img_array = []
for x in range(amountOfPictures):
    data = take_frame()
    print(x)
    w, h = 512, 512
    img = Image.fromarray(data, 'RGB')
    img.save('/home/pi/Desktop/Zeus/camera_test/fotos/'+str(x)+'.png')
    img = cv2.imread('/home/pi/Desktop/Zeus/camera_test/fotos/'+str(x)+'.png')
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)



out = cv2.VideoWriter('/home/pi/Desktop/Zeus/camera_test/video/'+ str(datetime.datetime.now()) + '.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()



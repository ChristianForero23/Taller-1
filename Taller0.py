import cv2
import numpy as np

class basicColor:

    def __init__(self, path):
        self.directorio = path
        self.image= cv2.imread(path)

    def displayProperties(self):
        h,w,c= self.image.shape
        print("Número de pixeles: {} , Número de canales: {}".format(h*w,c))

    def makeBW(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret2, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        return th1

    def colorize(self,h):
        HSV=cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
        HSV[:,:,0]=h
        return cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)



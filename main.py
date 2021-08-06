from Taller0 import *

path=input("ingrese entre comillas la ruta de la fotografia que desea procesar")
imagen= basicColor(path)
imagen.displayProperties()
cv2.imshow("Otsu",imagen.makeBW())
cv2.imshow(" ",imagen.colorize(100))
cv2.waitKey(0)
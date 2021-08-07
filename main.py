import cv2


""" TALLER_1 : Procesamiento de imagenes. Leer, extraer propiedades, binarizar y editar imagenes.
    
    Entradas: ruta de acceso a la imagen que se desea procesar.
    
    Metodos:  
            1. displayProperties -> permite el calculo del numero de pixeles y la cantidad de canales que componen la imagen de la clase.
            2. makeBW -> el metodo retorna una versión binaria, bajo el metodo de otsu, de la imagen de la clase. 
            3. colorize -> coloriza el canal hue de la imagen de la clase, la cual se encuentra representada en el espacio de color HSV.
                           el valor de colorización es solicitado al usuario, quien debe digitar un numero (entero) entre 0 179. 
"""


class basicColor:

    def __init__(self, path):
        self.directorio = path #ruta de acceso a la imagen
        self.image= cv2.imread(path) #imagen almacenada en self

    def displayProperties(self):
        h,w,c= self.image.shape #medidas y cantidad de canales de la imagen
        print("Número de pixeles: {} , Número de canales: {}".format(h*w*c,c))

    def makeBW(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)#imagen en escala de grises
        ret, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)# imagen binarizada bajo el metodo OTSU
        return otsu


    def colorize(self,h):
        HSV=cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)#transformación de la imagen al espacio HSV
        HSV[:,:,0]=h #modificacion del canal hue
        return cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)


if __name__ == '__main__':
    path=input("ingrese sin comillas la ruta de la fotografia que desea procesar")
    imagen= basicColor(path)
    imagen.displayProperties()
    cv2.imshow("Otsu",imagen.makeBW())
    h = int(input("Ingrese el valor hue [0-179] al que desea colorizar la imagen: "))
    cv2.imshow(" ",imagen.colorize(h))
    cv2.waitKey(0)


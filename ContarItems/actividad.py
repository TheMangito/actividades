import cv2
import numpy as np


def filterframe(color_bajo, color_alto, imagen, imagen_hsv):
    # Crear una máscara para el color rojo
    mascara_color = cv2.inRange(imagen_hsv, color_bajo, color_alto)

    # Convertir la imagen original a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Convertir la imagen gris a un formato BGR para que coincida con la original
    imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

    # Combinar la imagen en gris con las áreas en rojo
    resultado = np.where(mascara_color[:, :, None] == 255, imagen, imagen_gris_bgr)

    return resultado


imagen = cv2.imread('salida.png', 1)

# Convertir la imagen de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

color1_bajo = np.array([20, 40, 40])
color1_alto= np.array([30, 255, 255])

img_filtered = filterframe(color1_bajo, color1_alto, imagen, imagen_hsv)

alto, ancho, _ = img_filtered.shape
for i in range(alto):
    for j in range(ancho):
       if img_filtered[i, j] > 200:
           print("hola")
           




cv2.imshow("img", img_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
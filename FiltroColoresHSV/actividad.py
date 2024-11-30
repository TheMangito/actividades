import cv2
import numpy as np

"""
# Definir el rango de color rojo en HSV
bajo_rojo1 = np.array([0, 40, 40])
alto_rojo1 = np.array([10, 255, 255])
bajo_rojo2 = np.array([160, 40, 40])
alto_rojo2 = np.array([180, 255, 255])

# Crear una máscara para el color rojo
mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)
"""
# Leer la imagen en formato RGB
imagen = cv2.imread('arcoiris.jpg', 1)

# Convertir la imagen de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

color1_bajo = np.array([20, 40, 40])
color1_alto= np.array([30, 255, 255])

color2_bajo = np.array([65, 40, 40])
color2_alto= np.array([80, 255, 255])

color3_bajo = np.array([90, 40, 40])
color3_alto= np.array([100, 255, 255])

color4_bajo = np.array([100, 40, 40])
color4_alto= np.array([120, 255, 255])

color5_bajo = np.array([120, 40, 40])
color5_alto= np.array([140, 255, 255])

color6_bajo = np.array([10, 40, 40])
color6_alto= np.array([25, 255, 255])

def filtercolor(color_bajo, color_alto, title):
    # Crear una máscara para el color rojo
    mascara_color = cv2.inRange(imagen_hsv, color_bajo, color_alto)

    # Convertir la imagen original a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Convertir la imagen gris a un formato BGR para que coincida con la original
    imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

    # Combinar la imagen en gris con las áreas en rojo
    resultado = np.where(mascara_color[:, :, None] == 255, imagen, imagen_gris_bgr)

    # Mostrar la imagen final
    cv2.imshow(title, resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


filtercolor(color1_bajo, color1_alto, "color1")
filtercolor(color2_bajo, color2_alto, "color2")
filtercolor(color3_bajo, color3_alto, "color3")
filtercolor(color4_bajo, color4_alto, "color4")
filtercolor(color5_bajo, color5_alto, "color5")

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    if ret:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        #filtra tonalidades verdes
        img_filtered = filterframe(color2_bajo, color2_alto, img, hsv)
        cv2.imshow('hsv', img_filtered)
        k =cv2.waitKey(1) & 0xFF
        if k == 27 :
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
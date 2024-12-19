# Actividades Graficación

## 1 Contar ítems
En este código se lee una imagen (salida.png) y realiza un filtrado de color en el espacio HSV para resaltar un rango específico de tonalidades (color definido por *color1_bajo* y *color1_alto*). Después, convierte la imagen filtrada a escala de grises y combina las áreas filtradas con la imagen original, destacando ciertas regiones (por ejemplo, objetos de cierto color). Finalmente, recorre la imagen resultante píxel a píxel y realiza una comparación con el valor 200 para imprimir “hola” cada vez que encuentra un píxel con valor mayor a 200. En esencia, es un código inicial para contar o detectar píxeles que cumplan cierta condición de color y brillo.
```python
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
```

## 2 Primitivas
Dibuja primitivas gráficas (*rectángulos, círculos, polígonos*) sobre una imagen en blanco. Se genera un lienzo de **500x500** pixeles, se dibujan un rectángulo grande, varios círculos de diferentes colores y un polígono utilizando fillPoly. Finalmente muestra la imagen resultante. Es un ejemplo básico de dibujo de formas con OpenCV.
```python
import cv2 as cv
import numpy as np

img = np.ones((500, 500, 3), dtype=np.uint8)*255


cv.rectangle(img, (0, 300), (500, 0), (179, 214, 135), -1)
cv.circle(img, (120, 300), 120, (7,96,122), -1)
cv.circle(img, (240, 300), 90, (8,114,145), -1)
cv.rectangle(img,(0,500),(500,300),(29,230,181),-1) 
cv.circle(img, (390, 110), 50, (31,225,255), -1)
pts = np.array([[140, 300], [200, 300], [250, 500], [150, 500]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.fillPoly(img, [pts], (232, 177, 0))

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()

#3 Pelota Ping Pong y pelota que la evita
import numpy as np
import cv2 as cv

img = np.ones((300, 500, 1), dtype=np.uint8)*255

movimientoX = 1
movimientoY = 1

posicionP1X = 100
posicionP1Y = 100

while (True):
    posicionP1X += movimientoX
    posicionP1Y += movimientoY
    img = np.ones((300, 500, 1), dtype=np.uint8)*1
    cv.circle(img, (posicionP1X, posicionP1Y), 5, (255,255,255), -1)

    if (posicionP1X < 5 or posicionP1X > 500):
        movimientoX = -movimientoX
    if (posicionP1Y > 300 or posicionP1Y < 3):
        movimientoY = -movimientoY

    
    cv.imshow("imagen", img)
    cv.waitKey(10)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
```
## 3 Pelota Ping Pong y pelota que la evita
Crea una ventana y dibuja una pelota moviéndose dentro de un marco gris (**300x500** pixeles). La bola cambia de dirección al alcanzar los bordes. El movimiento es simulado en tiempo real. Este ejemplo demuestra animación básica de objetos **2D** (*una pelota*) rebotando en los límites de la ventana.
```python
import numpy as np
import cv2 as cv

img = np.ones((300, 500, 1), dtype=np.uint8)*255

movimientoX = 1
movimientoY = 1

posicionP1X = 100
posicionP1Y = 100

while (True):
    posicionP1X += movimientoX
    posicionP1Y += movimientoY
    img = np.ones((300, 500, 1), dtype=np.uint8)*1
    cv.circle(img, (posicionP1X, posicionP1Y), 5, (255,255,255), -1)

    if (posicionP1X < 5 or posicionP1X > 500):
        movimientoX = -movimientoX
    if (posicionP1Y > 300 or posicionP1Y < 3):
        movimientoY = -movimientoY

    
    cv.imshow("imagen", img)
    cv.waitKey(10)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()
```
## 4 Filtros HSV
Carga una imagen (*arcoiris.jpg*), la convierte a *HSV* y filtra rangos de color específicos para resaltar determinadas tonalidades. Además, muestra cómo aplicar el mismo tipo de filtrado a la captura en vivo de una cámara web (usando VideoCapture(0)). La función filtercolor muestra en ventanas separadas las regiones que cumplen el rango de cada color. Este código sirve de base para segmentación de colores en imágenes fijas y en video en tiempo real.
```python
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

```
## 5 Figura isométrica 2D representando 3D
Dibuja un conjunto de líneas que representan la proyección isométrica de una figura en **3D**, concretamente, un conjunto de vértices y aristas que dan la apariencia de un cubo o estructura compleja. Esto se logra proyectando puntos **3D** a coordenadas **2D** con proyección isométrica. Este ejemplo ilustra cómo generar proyecciones isométricas simples en **OpenCV**.
```python
import cv2
import numpy as np
import math

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 800

# Vértices del cubo en coordenadas 3D
vertices = np.array([
    [-1,1,1], #0
    [1,1,1], #1
    [-1,-1,-1], #2
    [1,1,-0.1], #3
    [-1,1,-0.1], #4
    [0.1,-0.3,-1], #5
    [-1,-1.2,-0.1], #6
    [-1,-1.25,-1], #7
    [-1,-2.25,-1], #8
    [-1,-0.2,-2], #9
    [-1,-1.2,-2], #10
    [-1,-2.25,1], #11
    [-1,-0.2,-3], #12
    [0,-0.1,-3], #13
    [-1,-1.2,-3], #14

])

# Conexiones de los vértices para formar las aristas del cubo
edges = [
    (0, 1),
    (1, 3),
    (0,4),
    (3,4),
    (3,5),
    (4,6),
    (6,7),
    (6,5),
    (7,9),
    (7,8),
    (9,10),
    (8,10),
    (0,11),
    (8,11),
    (9,12),
    (12,13),
    (5,13),
    (12,14),
    (10,14)

]

def project_isometric(vertex):
    """Función para proyectar un punto 3D a 2D con proyección isométrica"""
    x, y, z = vertex
    x2D = x - z
    y2D = (x + 2 * y + z) / 2
    return int(x2D * 100 + WIDTH / 2), int(-y2D * 100 + HEIGHT / 2)

# Crear ventana
cv2.namedWindow("Cubo Isométrico")

while True:
    # Crear imagen negra para el fondo
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Dibujar aristas del cubo
    for edge in edges:
        pt1 = project_isometric(vertices[edge[0]])
        pt2 = project_isometric(vertices[edge[1]])
        cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

    # Mostrar imagen
    cv2.imshow("Cubo Isométrico", frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```



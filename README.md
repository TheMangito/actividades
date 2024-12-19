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

## 6 Clonar Muñecos de nieve junto a casa OpenGL más Movimiento de cámara
En este codigo de OpenGL se renderiza una escena en **3D** con casas, muñecos de nieve y árboles. Se utiliza **GLFW** para crear la ventana y manejar las entradas del teclado, y **OpenGL** para dibujar cubos (*casas*), esferas (*muñecos de nieve*), cilindros y conos (*árboles, nariz del muñeco*), etc. Además, se permite mover la cámara en la escena con las teclas, simulando exploración en un entorno 3D. Este ejemplo demuestra el uso de OpenGL para construir escenas tridimensionales interactivas.

```python
Clonar Muñecos de nieve junto a casa OpenGL mas Movimiento de camara
import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluSphere, gluCylinder
import sys
import math

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 6, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    """Dibuja el cubo (base de la casa)"""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)  # Marrón para todas las caras

    # Frente
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(-1, 5, 1)

    # Atrás
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(-1, 5, -1)

    # Izquierda
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 5, 1)
    glVertex3f(-1, 5, -1)

    # Derecha
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(1, 5, -1)

    # Arriba
    glColor3f(0.9, 0.6, 0.3)  # Color diferente para el techo
    glVertex3f(-1, 5, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(1, 5, 1)
    glVertex3f(-1, 5, 1)

    # Abajo
    glColor3f(0.6, 0.4, 0.2)  # Suelo más oscuro
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

def draw_roof():
    """Dibuja el techo (pirámide)"""
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)  # Rojo brillante

    # Frente
    glVertex3f(-1, 5, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(0, 9, 0)

    # Atrás
    glVertex3f(-1, 5, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(0, 9, 0)

    # Izquierda
    glVertex3f(-1, 5, -1)
    glVertex3f(-1, 5, 1)
    glVertex3f(0, 9, 0)

    # Derecha
    glVertex3f(1, 5, -1)
    glVertex3f(1, 5, 1)
    glVertex3f(0, 9, 0)
    glEnd()

def draw_ground():
    """Dibuja un plano para representar el suelo o calle"""
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)  # Gris oscuro para la calle

    # Coordenadas del plano
    glVertex3f(-20, 0, 20)
    glVertex3f(20, 0, 20)
    glVertex3f(20, 0, -20)
    glVertex3f(-20, 0, -20)
    glEnd()

def draw_sphere(radius=1, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, 32, 32)
    glPopMatrix()

def draw_trunk():
    """Dibuja el tronco del árbol como un cilindro"""
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.1)  # Marrón para el tronco
    glTranslatef(0.0, 0.0, 0.0)  # Posicionar el tronco
    glRotatef(-90, 1, 0, 0)  # Rota para orientar el cilindro verticalmente
    quadric = gluNewQuadric()
    gluCylinder(quadric, 0.3, 0.3, 2.0, 32, 32)  # Radio y altura del cilindro
    glPopMatrix()

def draw_foliage():
    """Dibuja las hojas del árbol como una esfera"""
    glPushMatrix()
    glColor3f(0.1, 0.8, 0.1)  # Verde para las hojas
    glTranslatef(0.0, 2.0, 0.0)  # Posicionar las hojas encima del tronco
    quadric = gluNewQuadric()
    gluSphere(quadric, 1.0, 32, 32)  # Radio de la esfera
    glPopMatrix()


def draw_tree():
    """Dibuja un árbol completo"""
    draw_trunk()   # Dibuja el tronco
    draw_foliage() # Dibuja las hojas


def draw_cone(base=0.1, height=0.5, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 1, 0, 0)  # Orientar el cono hacia adelante
    quadric = gluNewQuadric()
    gluCylinder(quadric, base, 0, height, 32, 32)
    glPopMatrix()

def draw_snowman():
    # Cuerpo
    glColor3f(1, 1, 1)
    draw_sphere(1.0, 0, 0, 0)     # Base
    draw_sphere(0.75, 0, 1.2, 0)  # Cuerpo medio
    draw_sphere(0.5, 0, 2.2, 0)   # Cabeza

    # Ojos
    glColor3f(0, 0, 0)
    draw_sphere(0.05, -0.15, 2.3, 0.4)  # Ojo izquierdo
    draw_sphere(0.05, 0.15, 2.3, 0.4)   # Ojo derecho

    # Nariz (cono)
    glColor3f(1, 0.5, 0)  # Color naranja
    draw_cone(0.05, 0.2, 0, 2.2, 0.5)  # Nariz



def draw_house():
    """Dibuja una casa (base + techo)"""
    draw_cube()  # Base de la casa
    draw_roof()  # Techo

def draw_scene():
    """Dibuja toda la escena con casas"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(
        eje_x, eje_y, eje_z,
        eje_x + center_x, eje_y + center_y, eje_z + center_z,
        0.0, 1.0, 0.0
    )    # Vector hacia arriba

    # Dibujar el suelo
    draw_ground()

    # Dibujar las casas en diferentes posiciones
    positions = [
        (-5, 0, -5),  # Casa 1
    ]
    for pos in positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mover la casa a la posición actual
        draw_house()        # Dibujar la casa
        snowmanPos = (pos[0]+2, pos[1], pos[2])
        glTranslatef(*snowmanPos) 
        draw_snowman()
        glPopMatrix()

    glTranslate(7, 0, 7)
    draw_tree()

    glTranslate(eje_x, eje_y, eje_z)

    glfw.swap_buffers(window)

def avanzar_izq_der(is_izq):
    """Mueve la cámara a la izquierda o derecha"""
    global angulo_th, angulo_pi, radio
    global center_x, center_z
    global eje_x, eje_z
    global movimiento

    # Girar para la izquierda o derecha 90 grados
    if is_izq:
        angulo_th -= (math.pi / 2)
    else:
        angulo_th += (math.pi / 2)

    # Convertir coordenada esférica a rectangular (solo x y z)
    center_x = radio * math.sin(angulo_pi) * math.cos(angulo_th)
    center_z = radio * math.sin(angulo_pi) * math.sin(angulo_th)

    # Avanzar en x y z
    eje_x += center_x * movimiento
    eje_z += center_z * movimiento

    # Retornar al ángulo inicial
    if is_izq:
        angulo_th += (math.pi / 2)
    else:
        angulo_th -= (math.pi / 2)

    # Actualizar center_x y center_z
    center_x = radio * math.sin(angulo_pi) * math.cos(angulo_th)
    center_z = radio * math.sin(angulo_pi) * math.sin(angulo_th)

def key_callback(window, key, scancode, action, mods):
    """Manejo de eventos del teclado para mover la cámara"""
    global angulo_pi, angulo_th, saltos, radio
    global center_x, center_y, center_z
    global eje_x, eje_y, eje_z
    global movimiento

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_W:
            # Avanzar
            eje_x += center_x * movimiento
            eje_y += center_y * movimiento
            eje_z += center_z * movimiento
        elif key == glfw.KEY_S:
            # Retroceder
            eje_x -= center_x * movimiento
            eje_y -= center_y * movimiento
            eje_z -= center_z * movimiento
        elif key == glfw.KEY_A:
            # Mover a la izquierda
            avanzar_izq_der(True)
        elif key == glfw.KEY_D:
            # Mover a la derecha
            avanzar_izq_der(False)
        elif key == glfw.KEY_LEFT:
            # Girar a la izquierda
            angulo_th -= saltos
        elif key == glfw.KEY_RIGHT:
            # Girar a la derecha
            angulo_th += saltos
        elif key == glfw.KEY_UP:
            # Girar hacia arriba
            angulo_pi -= saltos
            if angulo_pi <= 0.0:
                angulo_pi = 0.001  # Evitar valor cero
        elif key == glfw.KEY_DOWN:
            # Girar hacia abajo
            angulo_pi += saltos
            if angulo_pi >= math.pi:
                angulo_pi = math.pi - 0.001  # Evitar exceder pi

        # Actualizar los valores de dirección
        center_x = radio * math.sin(angulo_pi) * math.cos(angulo_th)
        center_y = radio * math.cos(angulo_pi)
        center_z = radio * math.sin(angulo_pi) * math.sin(angulo_th)

def main():
    global window
    global radio
    global angulo_th 
    global angulo_pi
    global movimiento
    global saltos
    global eje_x
    global eje_y
    global eje_z
    global center_x
    global center_y
    global center_z

    radio = 1.0
    angulo_th = 3.9
    angulo_pi = 2.2

    saltos = 0.15
    movimiento = 0.8
    eje_x = 10.0
    eje_y = 2.0
    eje_z = 15.0

    # Inicializar la dirección inicial de la cámara
    center_x = radio * math.sin(angulo_pi) * math.cos(angulo_th)
    center_y = radio * math.cos(angulo_pi)
    center_z = radio * math.sin(angulo_pi) * math.sin(angulo_th)

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Escena con Casas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Configurar la función de callback para el teclado
    glfw.set_key_callback(window, key_callback)

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()

```
## 7 Operadores Puntuales
Lee una imagen en escala de grises (*logo1.png*) y aplica operaciones píxel a píxel para invertir colores, umbralizar, y asignar nuevos valores de brillo según condiciones (por ejemplo, si el píxel es mayor a cierto umbral asignar un valor específico, en caso contrario otro). Estas transformaciones punto a punto modifican el brillo y contraste de la imagen de forma manual. Se crean varias imágenes (*img1, img2, img3, etc...*) con diferentes criterios de cambio en el valor del píxel.

```python
import cv2 as cv


img = cv.imread('logo1.png', 0)

x, y = img.shape

img1 = img.copy()
for i in range(x):
    for j in range(y):
        if img1[i, j] == 0:
            img1[i, j] = 255
        else:
            img1[i, j] = 0

cv.imshow('img1', img1)

img2 = img.copy()
for i in range(x):
    for j in range(y):
        if img2[i, j] > 90:
            img2[i, j] = 150
        else:
            img2[i, j] = 100

cv.imshow('img2', img2)

img3 = img.copy()
for i in range(x):
    for j in range(y):
        if img3[i, j] > 120:
            img3[i, j] = 180
        else:
            img3[i, j] = 200

cv.imshow('img3', img3)

img4 = img.copy()
for i in range(x):
    for j in range(y):
        if img4[i, j] > 120:
            img4[i, j] = 180
        else:
            img4[i, j] = 200

cv.imshow('img4', img4)

img5 = img.copy()
for i in range(x):
    for j in range(y):
        if img5[i, j] > 150:
            img5[i, j] = 210
        else:
            img4[i, j] = 240

cv.imshow('img5', img5)

cv.waitKey(0)
cv.destroyAllWindows()


```

## 8 Flujo Óptico, Rastreo y Filtros
Captura video en tiempo real desde la cámara, selecciona ciertos puntos de interés (*p0*) y utiliza el método de Lucas-Kanade para el cálculo de flujo óptico (*seguimiento del movimiento de esos puntos entre fotogramas o frames consecutivos*). Se dibuja líneas y círculos para visualizar la trayectoria y compara distancias para detectar movimientos significativos. Este ejemplo ilustra cómo hacer seguimiento de puntos a lo largo de secuencias de imágenes (*video*).

```python
import numpy as np 
import cv2 as cv
import math

cap = cv.VideoCapture(0)


lkparm =dict(winSize=(15,15), maxLevel=2,
             criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)) 


_, vframe = cap.read()
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
p0 = np.array([(100,100), (200,100), (300,100), (400,100)
               ])

p0 = np.float32(p0[:, np.newaxis, :])

mask = np.zeros_like(vframe) 
cad =''

while True:
    _, frame = cap.read()
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm) 

    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.array([(100,100), (200,100), (300,100), (400,100) ])
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st ==1]
        bp0 = p0[st ==1]
        
        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())
            dist = np.linalg.norm(nv.ravel() - vj.ravel())
            
            
            
            frame = cv.line(frame, (c,d), (a,b), (0,0,255), 2)
            frame = cv.circle(frame, (c,d), 2, (255,0,0),-1)
            frame = cv.circle(frame, (a,b), 3, (0,255,0),-1)
            dist_magnitud = math.sqrt((a-c)**2+ (b-d)**2)
            if (dist_magnitud > 50 and dist):
                print("bolita "+ str(i) + " " + str(dist_magnitud))

        cv.imshow('ventana', frame)

        vgris = fgris.copy()

        if(cv.waitKey(1) & 0xff) == 27:
            break

cap.release()
cv.destroyAllWindows()
```
## 9 Investigación Ecuaciones Paramétricas

Las funciones paramétricas son una forma de representar curvas en el espacio mediante una o más variables independientes llamadas parámetros. A diferencia de las funciones normales (como *y=f(x)y = f(x)y=f(x)*), donde la relación entre las variables *x* y *y* es directa, en las funciones paramétricas tanto x como y (u otras variables) están definidas en función de un parámetro común, como ttt. Ejemplo básico de función paramétrica: Consideremos una curva en el plano. En lugar de describirla directamente como **y=f(x)y = f(x)y=f(x)**, podemos usar las funciones paramétricas: *x(t)=cos(t)x(t) = \cos(t)x(t)=cos(t) y(t)=sin(t)y(t) = \sin(t)y(t)=sin(t)* Aquí, **t** es el parámetro que toma valores dentro de un cierto intervalo. Al variar t, obtenemos los puntos **(x(t),y(t))(x(t), y(t))(x(t),y(t))** que trazan una circunferencia unitaria en el plano *xy*. Características de las funciones paramétricas:

- **Curvas en el espacio**: Se utilizan para representar curvas que no pueden expresarse fácilmente en la forma *y=f(x)y = f(x)y=f(x)*.
- **Movimiento: Los parámetros** pueden tener interpretaciones de tiempo, lo que permite describir el movimiento de un punto a lo largo de una curva.
- **Dimensiones adicionales**: Se pueden usar para describir curvas en el espacio tridimensional o en dimensiones más altas. Aplicaciones: • Cinemática: Para describir la trayectoria de un objeto en movimiento. • Gráficos por computadora: Se utilizan para generar formas y animaciones complejas. • Geometría: Para representar curvas y superficies que no tienen una representación algebraica simple.

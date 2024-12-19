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
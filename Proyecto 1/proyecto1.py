import numpy as np 
import cv2 as cv
import math

def trasladar_imagen(direccion, posicion, limite_min, limite_max):
    if direccion:  # Hacia la derecha
        if posicion + 30 < limite_max:
            posicion += 30
    else:  # Hacia la izquierda
        if posicion - 30 > limite_min:
            posicion -= 30
    return posicion

def escalar_imagen(imagen, scale_y, scale_x, capture):
    cap_x, cap_y = capture.shape[:2]
    imagen_x, imagen_y =imagen.shape[:2]
    
    if imagen_x*scale_x<cap_x and imagen_x*scale_x>50 and imagen_y*scale_y<cap_y and imagen_y*scale_y>0:
        scaled_img = cv.resize(imagen, None, fx=scale_x, fy=scale_y, interpolation=cv.INTER_LINEAR)
        return scaled_img
    return imagen  # Retorna la imagen original si las escalas están fuera de rango

def rotacion_imagen(r_imagen, angulo):
    (h, w) = r_imagen.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angulo, 1.0)
    image_rotated = cv.warpAffine(r_imagen, M, (w, h))
    return image_rotated

cap = cv.VideoCapture(0)

img = cv.imread("tnt.jpg")
if img is None:
    print("Error: no se pudo cargar la imagen.")
    exit(1)

x, y, c = img.shape
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

lkparm = dict(winSize=(15, 15), maxLevel=2,
              criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

_, vframe = cap.read()
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
p0 = np.array([(250, 120), 
               (250, 600), (1000, 200)
               ])

p0 = np.float32(p0[:, np.newaxis, :])

mask = np.zeros_like(vframe) 
cad = ''

posicion_x, posicion_y = 1280 // 2, 720 // 2
img_modify = img
umbral_min = 15  # Umbral mínimo para movimientos válidos
umbral_gesto = 30  # Umbral para reconocer gestos

while True:
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm) 

    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.array([(250, 120), 
                       (250, 600), (1000, 200)
                       ])
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st == 1]
        bp0 = p0[st == 1]

        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())
            dist_magnitud = math.sqrt((a - c) ** 2 + (b - d) ** 2)

            if dist_magnitud > umbral_min:  # Filtrar movimientos pequeños
                frame = cv.line(frame, (c, d), (a, b), (0, 125, 255), 2)
                frame = cv.circle(frame, (c, d), 2, (255, 255, 255), -1)
                frame = cv.circle(frame, (a, b), 3, (0, 0, 0), -1)

                if dist_magnitud > umbral_gesto:  # Reconocer gestos significativos
                    if i == 0:
                        if a - c > umbral_gesto:
                            img_modify = escalar_imagen(img_modify, 1.1, 1.1,frame)
                        elif a - c < -umbral_gesto:
                            img_modify = escalar_imagen(img_modify, 0.9, 0.9, frame)
                    elif i == 1:
                        if a - c > umbral_gesto:
                            img_modify = rotacion_imagen(img_modify, 90)
                        elif a - c < -umbral_gesto:
                            img_modify = rotacion_imagen(img_modify, -90)
                    elif i == 2:
                        if a - c > umbral_gesto:
                            posicion_x = trasladar_imagen(True, posicion_x, 0, frame.shape[1])
                        elif a - c < -umbral_gesto:
                            posicion_x = trasladar_imagen(False, posicion_x, 0, frame.shape[1])

        # Ajustar posiciones para evitar salir del marco
        alto_mod, ancho_mod, _ = img_modify.shape
        posicion_x = max(0, min(posicion_x, frame.shape[1] - ancho_mod))
        posicion_y = max(0, min(posicion_y, frame.shape[0] - alto_mod))

        frame[posicion_y:posicion_y + alto_mod, posicion_x:posicion_x + ancho_mod] = img_modify

        cv.imshow('ventana', frame)
        vgris = fgris.copy()

        if (cv.waitKey(1) & 0xff) == 27:
            break

cap.release()
cv.destroyAllWindows()

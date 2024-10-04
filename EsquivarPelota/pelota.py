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
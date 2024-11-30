import math
import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\sresm\Documents\ARCHIVOS TEMPORALES\Graficacion\logo1.png", 0)
x, y = img.shape
angle = 70
rotated_img = np.zeros((x*3, y*3), dtype=np.uint8)

xx, yy = rotated_img.shape
centro_x, centro_y = int(x  // 2), int(y  // 2)
radian_Angle = math.radians(angle)

for i in range(x):
    for j in range(y):
        
        new_x = int((int((j - centro_x) * math.cos(radian_Angle) - (i - centro_y) * math.sin(radian_Angle) + centro_x))*2)+20
        new_y = int((int((j - centro_x) * math.sin(radian_Angle) + (i - centro_y) * math.cos(radian_Angle) + centro_y))*2)+20
        if 0 <= new_x < y*3 and 0 <= new_y < x*3:
            rotated_img[new_y, new_x] = img[i, j]

cv.imshow("img", rotated_img)
cv.waitKey()
cv.destroyAllWindows()
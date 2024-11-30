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

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

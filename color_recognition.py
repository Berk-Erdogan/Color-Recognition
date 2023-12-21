import cv2
import numpy as np

img = cv2.imread("1.jpg")
img_new = cv2.resize(img, (300, 300))

hsv_frame = cv2.cvtColor(img_new, cv2.COLOR_BGR2HSV)

lower_bounds = [
    np.array([20, 100, 100]),  # Yellow
    np.array([100, 100, 100]),  # Blue
    np.array([0, 95, 100]),  # Red (1. gap)
    np.array([160, 95, 100]),  # Red (2. gap)
    np.array([40, 100, 100]),  # Green
    np.array([0, 0, 195]),  # White
    np.array([2, 100, 100])  # Orange
]

upper_bounds = [
    np.array([40, 255, 255]),  # Yellow
    np.array([130, 255, 255]),  # Blue
    np.array([20, 255, 255]),  # Red (1. gap)
    np.array([180, 255, 255]),  # Red (2. gap)
    np.array([80, 255, 255]),  # Green
    np.array([180, 100, 255]),  # White
    np.array([25, 255, 255])  # Orange
]

colors = ["Y", "B", "R", "R", "G", "W", "O"]

new_colors = np.zeros(9, dtype='U1')

location = [[50, 50],[150, 50],[250, 50],[50, 150],[150, 150],[250, 150],[50, 250],[150, 250],[250, 250]]

for x in range(7):
    mask = cv2.inRange(hsv_frame, lower_bounds[x], upper_bounds[x])

    p0 = mask[50, 50]
    p1 = mask[50, 150]
    p2 = mask[50, 250]
    p3 = mask[150, 50]
    p4 = mask[150, 150]
    p5 = mask[150, 250]
    p6 = mask[250, 50]
    p7 = mask[250, 150]
    p8 = mask[250, 250]

    pointerList = [p0, p1, p2, p3, p4, p5, p6, p7, p8]

    counter = 0
    for y in pointerList:
        if y == 255:
            new_colors[counter] = colors[x]
        counter += 1

for x in range(9):
    print(str(x) + ". " + "Color: " + new_colors[x])

f1 = cv2.FONT_ITALIC

for x in range(9):
    cv2.putText(img_new,str(x),(location[x][0],location[x][1]),f1,1,(40,40,40),cv2.LINE_4)

cv2.imshow('New',img_new)


cv2.waitKey(0)
cv2.destroyAllWindows()

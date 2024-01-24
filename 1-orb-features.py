import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)
orb = cv2.ORB_create()
kp = orb.detect(img, None)
kp, des = orb.compute(img, kp)
img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)

plt.imshow(img_kp)
plt.show()

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(img, None)
img_kp = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)

plt.imshow(img_kp)
plt.show()

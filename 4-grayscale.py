import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
plt.show()

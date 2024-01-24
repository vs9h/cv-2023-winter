import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg')
adjusted_img = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

plt.imshow(cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2RGB))
plt.show()

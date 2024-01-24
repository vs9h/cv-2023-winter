import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg')
img_moved = np.roll(img, 10, axis=1)

plt.imshow(cv2.cvtColor(img_moved, cv2.COLOR_BGR2RGB))
plt.show()

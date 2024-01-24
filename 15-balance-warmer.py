import cv2
import numpy as np

image = cv2.imread('pic.jpg')

blue_gain = 1.5
red_gain = 1.2

adjusted_image = np.zeros_like(image, dtype=np.float32)
adjusted_image[:, :, 0] = np.clip(image[:, :, 0] * blue_gain, 0, 255)
adjusted_image[:, :, 2] = np.clip(image[:, :, 2] * red_gain, 0, 255)
adjusted_image[:, :, 1] = image[:, :, 1]

adjusted_image = adjusted_image.astype(np.uint8)

cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

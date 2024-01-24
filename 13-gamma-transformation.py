import cv2
import numpy as np

image = cv2.imread('pic.jpg')

gamma = 1.5

gamma_corrected = np.power(image / 255.0, gamma) * 255.0
gamma_corrected = gamma_corrected.astype(np.uint8)

cv2.imshow('Original Image', image)
cv2.imshow('Gamma Corrected Image', gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()

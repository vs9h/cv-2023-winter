import cv2
import numpy as np

image = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))
_, binary_image = cv2.threshold(gradient_magnitude, 50, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # -1 draws all contours

cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.imshow('Contour Image (Sobel)', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

threshold_value = 128

_, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow('Binarized Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

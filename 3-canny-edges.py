import cv2

low_threshold=50
high_threshold=150
image = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred, low_threshold, high_threshold)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Eroded Image", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
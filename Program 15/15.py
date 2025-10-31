import cv2
import numpy as np
image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, 2, 3, 0.04)
harris_corners = cv2.dilate(harris_corners, None)
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]
cv2.imshow("Harris Corner Detection", image)
cv2.imwrite(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\harris_corners.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
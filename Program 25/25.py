import cv2
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")
image = cv2.imread(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
watches = watch_cascade.detectMultiScale(gray, 1.1, 5)
for (x,y,w,h) in watches:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Detected Watch", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture(r"D:\College\Year 2\CV_ITA0505\Practical\Programs\sample.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Playback", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

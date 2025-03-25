import cv2
import controller as cnt  # Updated code with motor control logic
from cvzone.HandTrackingModule import HandDetector

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Initialize webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)  # Flip frame horizontally
    hands, img = detector.findHands(frame)

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)  # Get fingers up status
        print(fingerUp)  # Debugging: Show finger status
        cnt.control_motor(fingerUp)  # Call the motor control function

        # Display the finger count on the frame
        finger_count_text = f"Finger count: {fingerUp.count(1)}"
        cv2.putText(frame, finger_count_text, (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # Show the frame
    cv2.imshow("Hand Gesture Control", frame)

    # Exit on 'k' key press
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()

import cv2 as cv
from segmenter import get_skin_mask
from detector import count_fingers
import os
os.environ["QT_LOGGING_RULES"] = "*.debug=false"

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)

    roi = frame[100:350, 400:600]

    #masking
    mask = get_skin_mask(roi)
    _, thresh = cv.threshold(mask, 127, 255, cv.THRESH_BINARY)

    #detection
    fingers = count_fingers(thresh, roi)

    cv.putText(frame, f"Fingers: {fingers}", (20, 50),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv.rectangle(frame, (400, 100), (600, 350), (0, 0, 255), 2)

    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask)

    if cv.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv.destroyAllWindows()
import cv2
from cv2 import aruco
import numpy as np

m_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param = aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    m_corner, m_IDs, reject = aruco.detectMarkers(
        gray, m_dict, parameters=param
    )
    if m_corner:
        for ids, corners in zip(m_IDs, m_corner):
            cv2.polylines(
                frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv2.LINE_AA
            )
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()
            cv2.putText(
                frame,
                f"id: {ids[0]}",
                top_right,
                cv2.FONT_HERSHEY_PLAIN,
                1.3,
                (200, 100, 0),
                2,
                cv2.LINE_AA,
            )
        
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("x"):
        break
cap.release()
cv2.destroyAllWindows()

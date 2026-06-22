import cv2
import os

def capture_face(name):
    cam = cv2.VideoCapture(0)
    count = 0

    path = f"media/faces/{name}"
    os.makedirs(path, exist_ok=True)

    while True:
        ret, frame = cam.read()
        cv2.imshow("Press S to save, Q to quit", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            cv2.imwrite(f"{path}/{count}.jpg", frame)
            count += 1

        if key == ord('q') or count >= 5:
            break

    cam.release()
    cv2.destroyAllWindows()
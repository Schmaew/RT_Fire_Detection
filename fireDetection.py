import cv2
from playsound import playsound
import time
import discord_test
import requests

fire_cascade = cv2.CascadeClassifier("fire_detection.xml")

payload = {"content": "5 second passed"}

payload2 = {"content": "10 second passed!!"}

newhead = {
    "authorization": "" # put discord authoriztion in here
}

cap = cv2.VideoCapture(0)
start_time = None  # Variable to store the start time of fire detection
fire_detected = False  # Flag to track if fire is currently detected

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    print(fire)
    if len(fire) > 0:
        if not fire_detected:
            # Start the timer only if fire was not detected in the previous frames
            start_time = time.time()
        fire_detected = True

        if time.time() - start_time >= 5:
            print(f"Fire detected for {round(time.time() - start_time)} seconds")
            requests.post(
                "", #put discord server url in here
                json=payload,
                headers=newhead,
            )

        if time.time() - start_time >= 10:
            print("ALARM! Fire detected for 10 seconds")
            requests.post(
                "", #put discord server url in here
                json=payload2,
                headers=newhead,
            )
            playsound("alarm.mp3")  # Replace with the actual alarm sound file
            start_time = None  # Reset the timer after triggering the alarm

        for x, y, w, h in fire:
            cv2.rectangle(
                frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2
            )

    else:
        # No fire detected in the current frame
        fire_detected = False
        start_time = None

    cv2.imshow("frame", frame)
    if cv2.waitKey(1000) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

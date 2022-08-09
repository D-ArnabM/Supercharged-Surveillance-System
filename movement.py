#made by amir bou
import cv2
import numpy as np
from raise_alert import Alert
import os
from twilio.rest import Client
#from send_sms import Sms

class Movement:
    def movement(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('movementoutput.avi', fourcc, 30.0, (640, 480))
        alert = Alert()
        #sms = Sms()
        count = 0
        cap = cv2.VideoCapture(0)#but your video here

        ret, frame1 = cap.read()
        ret, frame2 = cap.read()

        while cap.isOpened():
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5,5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)

                if cv2.contourArea(contour) < 5000:
                    continue
                cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 225, 0), 2)
                cv2.putText(frame1, "Detected".format("movement"), (10,20), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 225), 3)
                count = count + 1
                alert.play_audio()
                if count == 10:
                    message = client.messages \
                        .create(
                            body='ALERT : YOU HAVE AN UNKNOWN VISITOR',
                            from_='YOUR TWILIO ACCOUNTS PHONE NUMBER',
                            to='PHONE NUMBER OF THE SMS RECEIVER'
                        )
                    #sms.send()
                    count = 0
                hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                out.write(hsv)


            cv2.imshow("feed", frame1)
            frame1 = frame2
            ret, frame2 = cap.read()

            if cv2.waitKey(40) == 27:
                break

        cv2.destroyAllWindows()
        cap.release()


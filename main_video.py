import cv2
from simple_facerec import SimpleFacerec
from raise_alert import Alert
import os
from twilio.rest import Client
#from send_sms import Sms



def detect():
  
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
    alert = Alert()
    #sms = Sms()

    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")
    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        ret, frame = cap.read()

        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            if name == "Unknown":
                count = count + 1
                alert.play_audio()
                if count == 5:
                    message = client.messages \
                        .create(
                            body='ALERT : YOU HAVE AN UNKNOWN VISITOR',
                            from_='YOUR TWILIO NUMBER',
                            to='PHONE NUMBER OF SMS RECIEVER'
                        )
                    #sms.send()
                    count = 0
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(hsv) 
            else:
                continue    
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

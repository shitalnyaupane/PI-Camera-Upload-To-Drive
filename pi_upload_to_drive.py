from picamera import PiCamera
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from Google import Create_Service


camera  = PiCamera()
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
mime_types = ['application.vnd.openxmlformats-officialdocument.spreadsheetml.sheet', 'image/jpeg']


def capture_image():
    i = 1
    while(i<=5):
        camera.start_preview()
        camera.capture('/home/pi/Desktop/project/image/ex'+str(i)+'.jpg')
        print(f"picture {i} taken")
        time.sleep(1)
        i = i + 1
        camera.stop_preview()
capture_image()
        
def upload_image():
    
    for files in range(1, 6):
        f = "/home/pi/Desktop/project/image/ex" + str(files) + '.jpg'
        gfile = drive.CreateFile({'parents': [{'id': '1ZPuJj25y5DSbcXNrDDxNmzxGXjQIU_Tl'}]})
        gfile.SetContentFile(f)
        print(f"Opening file {files}")
        gfile.Upload()
        print(f"Uploaded file{files}")
                                 

upload_image()

import time,os
import winsound
from plyer import notification

#------------------------------constants---------------------------

INTERVAL = 30 # in minutes
TITLE = 'pani'
MESSAGE = 'drink the water' 

HOLD = 60 # notification display delay 

#------------------------------function----------------------------
def call():
    while True:
        notification.notify(
            title = TITLE,
            message = MESSAGE,
            timeout = HOLD
        )
        winsound.PlaySound("C:\programming\Python\Projects\Resources\sounds\pani.wav",winsound.SND_FILENAME)
        time.sleep(60 * INTERVAL) 
call()
#------------------------------call--------------------------------

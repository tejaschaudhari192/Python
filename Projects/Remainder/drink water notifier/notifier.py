import time,os
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
        time.sleep(60 * INTERVAL) 
call()
#------------------------------call--------------------------------

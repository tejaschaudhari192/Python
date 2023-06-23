import datetime
import time
from plyer import notification

while True:
    notification.notify(
        title = 'bhoju',
        message = 'hi',
        timeout = 60
    )
    time.sleep(60 * 30)

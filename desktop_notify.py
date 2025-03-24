import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!",
            message = "Take a break! Look 20m away for 20 sec",
            timeout = 20
        )
        time.sleep(1200)
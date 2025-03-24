from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time in HH:MM:SS AM/PM format: ").strip()

try:
    alarm_hour = int(alarm_time[0:2])
    alarm_min = int(alarm_time[3:5])
    alarm_sec = int(alarm_time[6:8])

    alarm_period = alarm_time[9:11].upper()

    print("Setting up alarm...")

    while True:
        now = datetime.now()
        curr_hour = int(now.strftime("%I")) # 12-hour format
        curr_min = int(now.strftime("%M"))
        curr_sec = int(now.strftime("%S"))
        curr_period = now.strftime("%p")

        print(f"Current Time: {curr_hour}:{curr_min}:{curr_sec} {curr_period}")

        if (alarm_period == curr_period):
            if (alarm_min == curr_min):
                if (alarm_sec == curr_sec):
                    print("Wake up!")
                    playsound('Gallan Mithiyan.mp3')
                    break
except ValueError:
    print("Invalid time format!")


    
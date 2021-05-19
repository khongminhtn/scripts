#!/usr/bin/python 
import psutil
import time
import csv

psutil.process_iter(attrs=None, ad_value=None)
hours = 0
minute = 0
with open("hours.py", "r") as file:
    hours = float(file.read())

while True:
    processes = []
    for line in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processes.append(line.name())
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if "pycharm64.exe" in processes or "Code.exe" in processes:
        with open("hours.py", "w") as file:
            hours += (1 / 60)
            if len(str(hours)) > 1:
                file.write(str(hours))
            else:
                print("hours empty")
            print("hours updated")
            print(f"1 minute spent programming. Total hours: {hours}")
    else:
        print("0 minutes spent on programming")
    time.sleep(60)


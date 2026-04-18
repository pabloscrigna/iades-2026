import time
from datetime import datetime


while True:
    with open("logs.txt", "a") as file:
        time.sleep(5)
        file.write(f"fecha hora: {datetime.now()}")


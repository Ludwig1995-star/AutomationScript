import time
from pynput.keyboard import Key, Controller
import schedule

keyboard = Controller()

def job():
    print("inicio!")
    time.sleep(5)
    keyboard.press(Key.f10)
    print("funciono!")

try:
    schedule.every().day.at("15:29").do(job)
except Exception as e:
    print(e)
    raise

while True:
    schedule.run_pending()
    time.sleep(1)

if _name_ == "_main_":
    job()
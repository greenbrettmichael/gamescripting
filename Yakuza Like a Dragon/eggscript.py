import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import pyautogui

start_stop_key = KeyCode(char='[')
exit_key = KeyCode(char=']')
keyboard = Controller()
delay = 0.25

class mainbotrunning(threading.Thread):
    def __init__(self, delay):
        super(mainbotrunning, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_botting(self):
        self.running = True

    def stop_botting(self):
        self.running = False

    def exit(self):
        self.stop_botting()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                pyautogui.keyDown("e")
                time.sleep(self.delay)
                pyautogui.keyUp("e")
            time.sleep(0.1)


bot_thread = mainbotrunning(delay)
bot_thread.start()


def on_press(key):
    if key == start_stop_key:
        if bot_thread.running:
            bot_thread.stop_botting()
        else:
            bot_thread.start_botting()
    elif key == exit_key:
        bot_thread.exit()
        listener.stop()
 

with Listener(on_press=on_press) as listener:
    listener.join()
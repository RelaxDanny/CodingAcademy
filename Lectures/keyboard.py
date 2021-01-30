from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

time.sleep(2)
keyboard.press(Key.ctrl)
keyboard.release(Key.ctrl)
time.sleep(2)
keyboard.press(Key.ctrl)
keyboard.release(Key.ctrl)
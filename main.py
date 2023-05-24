import time
import pyautogui
from PIL import ImageGrab


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def duck():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')


def detect_collision(image):

    # Adjust the coordinates based on your screen resolution
    roi = image.crop((170, 380, 230, 420))

    # Check if any pixel in the ROI is not white (indicating an obstacle)
    for pixel in roi.getdata():
        if pixel != (255, 255, 255):
            return True
    return False


def play_game():

    time.sleep(2)

    while True:
        # Capture the game screen
        screen = ImageGrab.grab()

        if detect_collision(screen):
            if detect_collision(screen.crop((80, 400, 120, 430))):
                duck()
            else:
                jump()

        time.sleep(0.1)


screenWidth, screenHeight = pyautogui.size()
print(screenWidth)
print(screenHeight)

pyautogui.moveTo(screenHeight/2, screenWidth/4)

pyautogui.click()

pyautogui.press('space')

play_game()

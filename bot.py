import pyautogui
import time
import keyboard
import threading
from PIL import Image
from tqdm import tqdm
import win32api, win32con
import virtualkeystroke as vkey
import os

# Function to simulate a mouse click at given coordinates
def click(x, y):
	win32api.SetCursorPos((x, y))
	win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, -1, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
	time.sleep(.05)


# Define coordinates for various actions
firstX, firstY = 644, 163
lastX, lastY = 1277, 796
openButtonX, openButtonY = 1093, 867
inputX, inputY = 1085, 759
closeButtonX, closeButtonY = 1347, 470

diffX = lastX - firstX
diffY = lastY - firstY
stepX = diffX / 31
stepY = diffY / 31
step = (stepX + stepY) / 2

        # Purchase Dialogue Checker #
purchase_check_topL = (831, 118)  # Example coordinates, replace with actual
purchase_check_bottomR= (1059,137)  # Example coordinates, replace with actual

pixels = {}

# Load the image and process its pixels | Now Includes error-handling
while True:
    imageName = input("Image name: ")

    # Check if the file exists
    if not os.path.isfile(imageName):
        print("Error: File not found. Please enter a valid file name.")
        continue

    try:
        # Open and process the image
        image = Image.open(imageName)
        if image.size[0] != 32 or image.size[1] != 32:
            print("Resizing image")
            image = image.resize((32, 32), resample=Image.BOX)
            image.save(imageName, quality=100)
        
        imagePixels = image.load()
        for x in range(32):
            for y in range(32):
                try:
                    pixels[imagePixels[x, y]].append([x, y])
                except KeyError:
                    pixels[imagePixels[x, y]] = [[x, y]]
        image.close()
        break  # Exit the loop if image processing is successful

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")


# Function to convert RGB to HEX
def rgb2hex(pixel):
	return '{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])


# Function to simulate a mouse click on a pixel
def clickPixel(clickX, clickY):
	click(clickX, clickY)


# Function to quickly simulate a mouse click on a pixel
def clickFastPixel(addX, addY):
	clickX = round(firstX + addX * stepX)
	clickY = round(firstY + addY * stepY)
	clickPixel(clickX, clickY)


# Function to check and click a pixel with a specific color
def clickCheckPixel(addX, addY, color, s):
	clickX = round(firstX + addX * stepX)
	clickY = round(firstY + addY * stepY)
	pixelColor = s.getpixel((clickX, clickY))
	if pixelColor[0:3] == color[0:3]:
		return False
	selectColor(color)
	clickPixel(clickX, clickY)
	# print(f"{pixelColor[0:3]} -> {color[0:3]}")
	return True


# Function to select a color in the game
def selectColor(color):
	hexColor = rgb2hex(color)
	click(openButtonX, openButtonY)
	time.sleep(.05)
	click(inputX, inputY)
	time.sleep(.05)
	vkey.typer(string=hexColor)
	time.sleep(.05)
	click(closeButtonX, closeButtonY)

# Function to check for purchase dialogue
def check_purchase_dialogue(screenshot):
    purchase_color_hex = 'ec726b'  # Drawing Canvas background (usually bright pinkish)

    for x in range(purchase_check_topL[0], purchase_check_bottomR[0]):
        for y in range(purchase_check_topL[1], purchase_check_bottomR[1]):
            color = screenshot.getpixel((x, y))
            if rgb2hex(color) != purchase_color_hex:
                return True
    return False


# Main execution 
inputVar = input("Use FastPixel? ")

# Zoom-fix #
# Zooms In
pyautogui.keyDown('i')
time.sleep(3.5)
pyautogui.keyUp('i')

# Zooms out (Press 'O' 3 times)
for _ in range(3):
    pyautogui.press('o')
    time.sleep(0.01)  # Short delay between presses


click(closeButtonX, closeButtonY)
click(closeButtonX, closeButtonY)

time.sleep(0.05)

pause_flag = threading.Event()
quit_flag = threading.Event()

def check_keys(): # Pause Process
    while not quit_flag.is_set():
        if keyboard.is_pressed('p'):
            if pause_flag.is_set():
                print("Resuming...")
                pause_flag.clear()
            else:
                print("Paused. Press 'p' again to continue.")
                pause_flag.set()
            time.sleep(0.3)  # Debounce to prevent multiple toggles
        if keyboard.is_pressed('q'):
            quit_flag.set()
            break
        time.sleep(0.01)

key_thread = threading.Thread(target=check_keys)
key_thread.start()

if inputVar == "y":
    for color in tqdm(pixels):
        selectColor(color)
        for pixel in pixels[color]:
            clickFastPixel(pixel[0], pixel[1])
            if quit_flag.is_set():
                quit()
            while pause_flag.is_set():
                time.sleep(0.05)

while not quit_flag.is_set(): # Quit process
    s = pyautogui.screenshot()
    if check_purchase_dialogue(s):
        print("Purchase dialogue detected, pressing ESC.")
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(0.5)
        continue

    changedPixel = False
    time.sleep(0.01)  
    for color in tqdm(pixels):
        for pixel in pixels[color]:
            if clickCheckPixel(pixel[0], pixel[1], color, s):
                changedPixel = True
            if quit_flag.is_set():
                quit()
            while pause_flag.is_set():
                time.sleep(0.01)  
    if not changedPixel:
        break
    click(closeButtonX, closeButtonY)
    time.sleep(0.01)  

quit_flag.set()
key_thread.join()

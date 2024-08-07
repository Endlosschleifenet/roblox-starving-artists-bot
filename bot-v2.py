import pyautogui
import time
import keyboard
import threading
from PIL import Image
from tqdm import tqdm
import win32api, win32con
import virtualkeystroke as vkey
import random
import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to validate user input for time options
def get_time_option():
    while True:
        clear_screen()
        print("Choose a click speed option:")
        print("1. Human-like (6 seconds)")
        print("2. Quicker (1 second)")
        print("3. Balanced (0.5 seconds)")
        print("4. Swift (0.26 seconds)")
        print("5. Advanced")
        
        option = input("Enter a number (1-5): ")

        if option == '1':
            return 6
        elif option == '2':
            return 1
        elif option == '3':
            return 0.5
        elif option == '4':
            return 0.26
        elif option == '5':
            return advanced_options()
        else:
            print("Error: Invalid option. Please enter a number between 1 and 5.")
            time.sleep(2)  # Wait for 2 seconds before re-prompting

# Function to handle advanced options
def advanced_options():
    while True:
        clear_screen()
        print("Advanced Options:")
        print("1. Experimental")
        print("2. Custom Time")
        print("3. Back")
        
        option = input("Enter a number (1-3): ")
        
        if option == '1':
            if solve_puzzle():
                return 0.1  # Example of an experimental speed
            else:
                print("Error: Incorrect puzzle solution. Returning to Advanced Options.")
                time.sleep(2)
        elif option == '2':
            while True:
                clear_screen()
                custom_time = float(input("Enter custom time (must not be below 0.26 seconds): "))
                if custom_time >= 0.26:
                    return custom_time
                else:
                    print("Error: Time must not be below 0.26 seconds.")
                    time.sleep(2)
        elif option == '3':
            return get_time_option()
        else:
            print("Error: Invalid option. Please enter a number between 1 and 3.")
            time.sleep(2)

# Function to present a random math puzzle
def solve_puzzle():
    clear_screen()
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-'])
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    user_answer = float(input(f"Solve this puzzle to continue: {num1} {operation} {num2} = "))
    return user_answer == correct_answer

# Get user choice for click delay time
click_delay = get_time_option()

# Function to simulate a mouse click at given coordinates
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, -1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(click_delay)  # Use the chosen delay time for sleep

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

# Purchase Dialogue Checker
purchase_check_topL = (831, 118)
purchase_check_bottomR = (1059, 137)

pixels = {}

# Load the image and process its pixels
while True:
    clear_screen()
    imageName = input("Image name: ")

    if not os.path.isfile(imageName):
        print("Error: File not found. Please enter a valid file name.")
        time.sleep(2)
        continue

    try:
        image = Image.open(imageName)
        if image.size != (32, 32):
            print("Resizing image")
            image = image.resize((32, 32), resample=Image.BOX)
            image.save(imageName, quality=100)
        
        imagePixels = image.load()
        for x in range(32):
            for y in range(32):
                pixels.setdefault(imagePixels[x, y], []).append((x, y))
        image.close()
        break

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        time.sleep(2)

# Function to convert RGB to HEX
def rgb2hex(pixel):
    return '{:02x}{:02x}{:02x}'.format(*pixel[:3])

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
    if pixelColor[:3] == color[:3]:
        return False
    selectColor(color)
    clickPixel(clickX, clickY)
    return True

# Function to select a color in the game
def selectColor(color):
    hexColor = rgb2hex(color)
    click(openButtonX, openButtonY)
    time.sleep(0.001)
    click(inputX, inputY)
    time.sleep(0.001)
    vkey.typer(string=hexColor)
    time.sleep(0.001)
    click(closeButtonX, closeButtonY)

# Function to check for purchase dialogue
def check_purchase_dialogue(screenshot):
    purchase_color_hex = 'ec726b'
    for x in range(purchase_check_topL[0], purchase_check_bottomR[0]):
        for y in range(purchase_check_topL[1], purchase_check_bottomR[1]):
            color = screenshot.getpixel((x, y))
            if rgb2hex(color) != purchase_color_hex:
                return True
    return False

# Main execution
clear_screen()
inputVar = input("Use FastPixel? ")

click(closeButtonX, closeButtonY)
click(closeButtonX, closeButtonY)

# Zoom-fix
print("Zooming in...")
keyboard.press('i')
time.sleep(3.5)
keyboard.release('i')
print("Zoom in completed.")

# Zooming out
print("Zooming out...")
i = 0
while i < 3:
    keyboard.press('o')
    time.sleep(0.01)  # Small delay to ensure the key press is registered
    keyboard.release('o')
    time.sleep(0.01)
    i += 1
print("Zoom out completed.")

time.sleep(0.01)

pause_flag = threading.Event()
quit_flag = threading.Event()

def check_keys():  # Pause Function
    while not quit_flag.is_set():
        if keyboard.is_pressed('p'):
            if pause_flag.is_set():
                clear_screen()
                print("Resuming...")
                pause_flag.clear()
            else:
                clear_screen()
                print("Paused. Press 'p' again to continue.")
                pause_flag.set()
            time.sleep(0.25)  # Debounce to prevent multiple toggles
        if keyboard.is_pressed('q'):
            clear_screen()
            print("Quitting...")
            quit_flag.set()
            break
        time.sleep(0.01)
    quit()  # Ensure quit is called when quit_flag is set

key_thread = threading.Thread(target=check_keys)
key_thread.start()

if inputVar == "y":
    for color in tqdm(pixels):
        selectColor(color)
        for pixel in pixels[color]:
            clickFastPixel(pixel[0], pixel[1])
            if quit_flag.is_set():
                break
            while pause_flag.is_set():
                time.sleep(0.05)
        if quit_flag.is_set():
            break

while not quit_flag.is_set():
    s = pyautogui.screenshot()
    if check_purchase_dialogue(s):
        clear_screen()
        print("Purchase dialogue detected, pressing ESC.")
        pyautogui.press('esc')
        pyautogui.press('esc')
        time.sleep(0.25)
        continue

    changedPixel = False
    time.sleep(0.01)
    for color in tqdm(pixels):
        for pixel in pixels[color]:
            if clickCheckPixel(pixel[0], pixel[1], color, s):
                changedPixel = True
            if quit_flag.is_set():
                break
            while pause_flag.is_set():
                time.sleep(0.01)
        if quit_flag.is_set() or not changedPixel:
            break
    click(closeButtonX, closeButtonY)
    time.sleep(0.01)

quit_flag.set()
key_thread.join()

# End
keyboard.press('p')
time.sleep(0.001)
keyboard.release('p')

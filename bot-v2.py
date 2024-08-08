import pyautogui
import time
import keyboard
import threading
from PIL import Image
from tqdm import tqdm
import win32api, win32con
import virtualkeystroke as vkey
import os
import sys
import random
global click_delay, description, fast_pixel_option


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

# Purchase Dialogue Checker
purchase_check_topL = (831, 118)  # Example coordinates, replace with actual
purchase_check_bottomR = (1059, 137)  # Example coordinates, replace with actual

pixels = {}
click_delay = 1.0
description = "Default"
fast_pixel_option = False

# Function to check Python version is "adequate"
def check_python_version():
    version_info = sys.version_info
    if (version_info.major == 3 and 
        8 <= version_info.minor <= 12 and 
        version_info.minor != 10):
        countdown_message(f"Python version {version_info.major}.{version_info.minor} is acceptable.", 2)
    else:
        print(f"Python version {version_info.major}.{version_info.minor} is not supported.")
        print("This script requires Python version between 3.8 and 3.12, but not 3.10.")
        print("")
        input("Press any key to continue...")
        sys.exit(1)

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display a countdown message
def countdown_message(message, seconds):
    clear_screen()
    print(message)
    for i in range(seconds, 0, -1):
        print(f"\r{i} second{'s' if i > 1 else ''}...", end='', flush=True)
        time.sleep(1)
    print()

# Function to handle advanced options
def advanced_options():
    while True:
        clear_screen()
        print("Advanced Options:")
        print("1. Experimental")
        print("2. Custom Time")
        print("3. Back")
        
        option = input("Enter a number (1-3): ").strip()
        
        if option == '1':
            if solve_puzzle():
                while True:
                    clear_screen()
                    print("! WARNING !")
                    time.sleep(1)
                    print("Using values lower than 0.26 may cause system instability")
                    time.sleep(1)
                    print("or at best some pixels on the canvas to be skipped.")
                    time.sleep(1)
                    print("Remember to use Ctrl + Alt + Delete in an emergency")
                    time.sleep(1)
                    print("Developers are NOT liable for any incorrect settings set here.")
                    time.sleep(1)
                    print("Please agree that you are liable for any damages below,")
                    time.sleep(1)    
                    print("otherwise you cannot use Experiments.")
                    time.sleep(2)      
                    print("")
                    time.sleep(0.5)
                    
                    agree = input("I Agree: [Y/N]? ").strip().lower()
                    if agree != "y":
                        return get_time_option()
                    
                    try:
                        clear_screen()
                        countdown_message("Warning Acknowledged!", 2)
                        clear_screen()
                        custom_time = float(input("Enter experimental time (any float number): ").strip())
                        return custom_time, "Experimental"
                    except ValueError:
                        print("Error: Invalid input. Please enter a valid float number.")
                        countdown_message("Error: Invalid input. Please enter a valid float number.", 2)
            else:
                print("Error: Incorrect puzzle solution. Returning to Advanced Options.")
                countdown_message("Error: Incorrect puzzle solution. Returning to Advanced Options.", 2)
        elif option == '2':
            while True:
                clear_screen()
                try:
                    custom_time = float(input("Enter custom time (must be 0.26 seconds or more): ").strip())
                    if custom_time >= 0.26:
                        return custom_time, "Custom Time"
                    else:
                        print("Error: Custom time must be 0.26 seconds or more.")
                        countdown_message("Error: Custom time must be 0.26 seconds or more.", 2)
                except ValueError:
                    print("Error: Invalid input. Please enter a valid float number.")
                    countdown_message("Error: Invalid input. Please enter a valid float number.", 2)
        elif option == '3':
            return get_time_option()
        else:
            print("Error: Invalid option. Please enter a number between 1 and 3.")
            countdown_message("Error: Invalid option. Please enter a valid number.", 2)

# Function to validate user input for time options
def get_time_option():
    while True:
        clear_screen()
        print("Choose a click speed option:")
        print("1. Human-like (3 seconds)")
        print("2. Quicker (0.7 seconds)")
        print("3. Balanced (0.5 seconds)")
        print("4. Swift (0.26 seconds)")
        print("5. Advanced")
        
        option = input("Enter a number (1-5): ").strip()

        if option == '1':
            click_delay = 3
            description = "Human-like"
        elif option == '2':
            click_delay = 0.7
            description = "Quicker"
        elif option == '3':
            click_delay = 0.5
            description = "Balanced"
        elif option == '4':
            click_delay = 0.26
            description = "Swift"
        elif option == '5':
            click_delay, description = advanced_options()
            clear_screen()
        else:
            countdown_message("Error: Invalid option. Please enter a valid number.", 2)
            continue

        clear_screen()
        print(f"{description} ({click_delay} seconds)...")
        time.sleep(1)  # Wait a second to display the chosen option
        print("Loaded!")
        time.sleep(1)  # Wait another second before proceeding
        return click_delay, description

# Function to present a random math puzzle
def solve_puzzle():
    clear_screen()
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-'])
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    
    try:
        user_answer = float(input(f"Solve this puzzle to continue: {num1} {operation} {num2} = ").strip())
        return user_answer == correct_answer
    except ValueError:
        print("Error: Please enter a valid number.")
        return False

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
    return True

# Function to select a color in the game
def selectColor(color):
    hexColor = rgb2hex(color)
    click(openButtonX, openButtonY)
    time.sleep(0.01)
    click(inputX, inputY)
    time.sleep(0.01)
    vkey.typer(string=hexColor)
    time.sleep(0.01)
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

# Function to load and process the image
def load_image():
    global pixels
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

# Confirm the settings with the user
def confirm_settings(click_delay, image_name, fast_pixel_option, description):
    clear_screen()
    print(f"Click Speed Description: {description} ({click_delay} seconds)")
    print(f"Image File: {image_name}")
    print(f"Fast Pixel Option: {fast_pixel_option}")
    time.sleep(1)
    print()
    time.sleep(1)

    confirm = input("Are you satisfied with the settings? (yes/no): ").strip().lower()
    if confirm in ['y', 'yes']:
        return True
    else:
        return False

# Check Python version
check_python_version()


click_delay, description = get_time_option()

# Function to simulate a mouse click at given coordinates
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, -1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(click_delay)

# Main function to execute actions
def main_exec():

    # Prompt user for fast pixel option
    while True:
        clear_screen()
        fast_pixel_option = input("Enable fast pixel option? [Y/N]: ").strip().lower() == 'y'
        if fast_pixel_option in [True, False]:
            break
        print("Error: Invalid input. Please enter 'Y' or 'N'.")
        countdown_message("Error: Invalid input. Please enter 'Y' or 'N'.", 2)

    # Load the image
    load_image()

    click(closeButtonX, closeButtonY) # Focus roblox
    time.sleep(0.02) # Wait for registration
    click(closeButtonX, closeButtonY) # Clicks close on colour picker just incase its open
    # Zoom-fix
    print("Zooming in...")
    keyboard.press('i')  # Simulate pressing down the 'i' key
    time.sleep(3.5)       # Hold the key down for 3.5 seconds
    keyboard.release('i')  # Release the 'i' key
    print("Zoom in completed.")

    # Zooming out
    print("Zooming out...")
    for i in range(1):
        keyboard.press('o')  # Press the 'o' key
        time.sleep(0.02)  # Delay to help the key register properly
        keyboard.release('o') # Release the 'o' key
        
    print("Zoom out completed.")

    time.sleep(0.01)

    pause_flag = threading.Event()
    quit_flag = threading.Event()

    def check_keys():
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

    if fast_pixel_option:
        for color in tqdm(pixels):
            selectColor(color)
            for pixel in pixels[color]:
                clickFastPixel(pixel[0], pixel[1])
                if quit_flag.is_set():
                    quit()
                while pause_flag.is_set():
                    time.sleep(0.01)

    while not quit_flag.is_set():
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

    quit()

# Run the main function
if __name__ == "__main__":
    main_exec()

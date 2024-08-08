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

# Define coordinates for various actions | Must be changed
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

purchase_check_topL = (831, 118)  # Example coordinates, replace with actual
purchase_check_bottomR= (1059,137)  # Example coordinates, replace with actual

# Global variables
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
                        countdown_message("Warning Acknowledged!",2)
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

# Checks if the canvas pixels are still changing
def check_pixel_changes(screenshot, region, last_pixels):
    x1, y1, x2, y2 = region
    unchanged = True
    current_pixels = {}
    
    # Iterate through the defined region
    for x in range(x1, x2):
        for y in range(y1, y2):
            pixel = screenshot.getpixel((x, y))
            current_pixels[(x, y)] = pixel
            if (x, y) not in last_pixels or last_pixels[(x, y)] != pixel:
                unchanged = False
    
    return unchanged, current_pixels

# Function to convert RGB to HEX
def rgb2hex(pixel):
    return '{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])

# Function to simulate a mouse click at given coordinates
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, -1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    time.sleep(0.05)

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
    if fast_pixel_option:
        clickFastPixel(addX, addY)
    else:
        clickPixel(clickX, clickY)
    s += 1
    time.sleep(click_delay)
    return s

# Function to perform actions within a specific region
def perform_actions_in_region(region, max_loops=1000):
    s = 0
    iteration = 0
    last_pixels = {}
    clear_screen()
    
    # Main loop
    while iteration < max_loops:
        iteration += 1
        screenshot = pyautogui.screenshot(region=region)
        unchanged, last_pixels = check_pixel_changes(screenshot, region, last_pixels)

        if unchanged:
            print("Pixels unchanged. Taking action...")
            s = clickCheckPixel(7, 7, "00644F", s)
        else:
            print("Pixels changed.")
        
        # Check for termination key
        if keyboard.is_pressed("q"):
            print("Termination key pressed. Exiting.")
            break

    print(f"Completed {iteration} iterations.")
    print(f"Clicks: {s}")

# Main function to execute actions
def main_exec():
    global click_delay, description, fast_pixel_option
    click_delay, description = get_time_option()
    
    # Prompt user for fast pixel option
    while True:
        clear_screen()
        fast_pixel_option = input("Enable fast pixel option? [Y/N]: ").strip().lower() == 'y'
        if fast_pixel_option in [True, False]:
            break
        print("Error: Invalid input. Please enter 'Y' or 'N'.")
        countdown_message("Error: Invalid input. Please enter 'Y' or 'N'.", 2)
    
    # Perform actions
    region = (firstX, firstY, diffX, diffY)
    perform_actions_in_region(region)

# Run the main function
if __name__ == "__main__":
    check_python_version()
    main_exec()

# [Starving Artists](https://www.roblox.com/games/8916037983/starving-artists-DONATION-GAME) bot (Roblox Game) | [Original Repository](https://github.com/Luois45/roblox-starving-artists-bot) from [Luois45](https://github.com/Luois45) 
### This fork packs some improvements over the old repository including efficiency and error-handling.

# Roblox Starving Artists Automation Bot

This repository contains a script designed to automate painting actions in the Roblox game "Starving Artists". It uses image recognition and simulates mouse and keyboard actions to paint based on a provided image.

> [!NOTE]
> From Luois45: This is a project I made a while ago and just wanted to share with the community. While I don't plan on further developing it, I'll still maintain it and address any issues that may arise.

> [!WARNING]
> Using this script can theoretically get you banned from the game or Roblox platform. It's specifically designed for the "Starving Artists" game on Roblox. Use at your own risk and always respect the terms of service of the game and platform.

## Table of Contents
* [Features](#features)
* [Perequisites](#perequisites)
* [Windows Installation](#windows-installation)
* [Unix Installation (Mac OS, Linux, etc.,)](#unix-installation)
* [Usage](#usage)
* [Contributing](#contributing)
  ### Others
* [Issues](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/issues)
* [Discussions](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/discussions)
* [Original Repository](https://github.com/Luois45/roblox-starving-artists-bot)

## Features
* Included from [Original Repository](https://github.com/Luois45/roblox-starving-artists-bot) by [Luois45](https://github.com/Luois45):
  * Simulates mouse clicks and movements based on the provided image
  * Converts the image into a format suitable for the game
  * Can be compiled into a standalone executable
  * Supports 32x32 and larger images
* My own Improvements:
  * Includes co-ordinate finding | [coordinates-finder.py](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/blob/main/coordinates-finder.py)
  * Image file-search Error-handling
  * Roblox Purchase Dialogue box "guard" - Meant to protect you from pesky dialogue boxes for robux (Beta)
  * Pause (With letter P) **Will resume when "P" is pressed again regardless of if you're off of Roblox or in a chatbox!
  * Improved Pause and Quit handling
  * Faster painting generation (This "claim" may vary, but has been seen to, generally, be faster!)
  * Better README
  * Zoom-fix (resolves an issue where when Roblox's "Spatial Chat" mute/unmute button causes some pixels on the canvas to be un-drawable)
  * Optimised, re-made UI
  * Easy access to change Click-speed (How fast the bot draws the painting) along with presets and customisation
  * Input Error-Handling
  * Some code-cleanup
  * Bug fixes(?)

> [!NOTE]
> My newer edits are in a temporary file called [bot-v2.py](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/blob/main/bot-v2.py).

## Perequisites

-   Python 3.8-3.9, 3.11-3.12 (Recommended: 3.8+, 3.10 includes a bug that causes pyinstaller to, apparently have errors) [Python Downloads](https://www.python.org/downloads/)

## Windows Installation

1: Go to https://github.com/Endlosschleifenet/roblox-starving-artists-bot/
2: Find the `Releases` section
<details>
 <summary>Illustration</summary>
 ![photo_2024-08-07_06-47-55](https://github.com/user-attachments/assets/d6e61ff1-66f5-46b5-9be4-4415aa0b352f)
3: Choose what you'd like from the release
 
</details>


## Unix Installation


  ## Simple Installation (Recommended)
  See [Windows Installation](https://github.com/your-repo/README.md#windows-installation) for details!


<details>
  <summary>Using Terminal/Shell window (Advanced)</summary>
Note: This requires your system to have git installed. Verify you have it installed by opening a shall/terminal and typing the following:
```batch
git --version
```
<details>![image](https://github.com/user-attachments/assets/386d685f-ef85-49c6-908f-11ae68b389a7)
</details>

1. Clone the repository:

```batch
git clone (https://github.com/Endlosschleifenet/roblox-starving-artists-bot
```
<details>![image](https://github.com/user-attachments/assets/c39dca71-e3db-474d-84f4-fb8e9683d25e)
</details>

2. Navigate to the project directory:

```batch
cd roblox-starving-artist-bot
```

3. Install the required packages:

```batch
pip install -r requirements.txt
```
</details>
</details>

## Usage

>[!TIP]
> The bot.py in this repository are the optimised settings for a full-screen 1920x1080 screen.

1. Start the "[Starving Artists](https://www.roblox.com/games/8916037983/starving-artists-DONATION-GAME)" game on Roblox
2. Position the game window appropriately (Fullscreen is recommended for 1920x1080 screens)

3. Run the bot by clicking on bot.py or by typing `py bot.py`

4. Follow on-screen instructions

5. If any help is required make a bug report with the tag `#assistance`

## Contributing

Feel free to change, modify, fork, edit, pull whatever! The License allows changes without need for permission or discussion. If you'd like to discuss any bugs or changes or make a pull request feel more than free!

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

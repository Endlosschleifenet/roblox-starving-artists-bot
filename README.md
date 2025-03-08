> [!CAUTION]
> My newest implementation, [bot-v2.py](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/blob/main/bot-v2.py) includes code that is not entirely tested and, in it's own way, is experimental itself. If any bugs arise, please report them in [Issues](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/issues)!

# [Starving Artists](https://www.roblox.com/games/8916037983/starving-artists-DONATION-GAME) bot (Roblox Game) | [Original Repository](https://github.com/Luois45/roblox-starving-artists-bot) from [Luois45](https://github.com/Luois45) 
### This fork packs some improvements over the old repository including efficiency and error-handling.

![Alt](https://repobeats.axiom.co/api/embed/dd69147f91b4d46e115a2e19bd584ef7ae1d6ea5.svg "Repobeats analytics image")

# Roblox Starving Artists Automation Bot

This repository contains a script designed to automate painting actions in the Roblox game "Starving Artists". It uses image recognition and simulates mouse and keyboard actions to paint based on a provided image.

> [!NOTE]
> From Luois45: This is a project I made a while ago and just wanted to share with the community. While I don't plan on further developing it, I'll still maintain it and address any issues that may arise.

> [!WARNING]
> Using this script can theoretically get you banned from the game or Roblox platform. It's specifically designed for the "Starving Artists" game on Roblox. Use at your own risk and always respect the terms of service of the game and platform.

> [!CAUTION]
> **This code (by my implementation) now includes advanced and experimental options. Neither me,  Luois45 or any contributor can be held liable for any incorrect settings in Experimental options. If you intend to use Experimental options in the code, there is an agreement in order to use the feature, otherwise you'll be sent back to the main options.**

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
* [Contact Info](#contact-info)

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
  * Code will stop upon canvas completion
  * Can make more canvases after your current canvas is finished generating
  * Overhauled UI
  * Python Version Check
* Upcomming:
  * Adjust the co-ordinates of everything.
  * A wiki? (Including Explanations of things etc.)
  * Requirements check and auto-install

> [!NOTE]
> My newer edits are in a temporary file called [bot-v2.py](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/blob/main/bot-v2.py). **Upcomming features are only a snapshot of what could come to this project. It isn't a promise and changes can always happen.

## Perequisites

-   Python 3.8-3.9, 3.11-3.12 (Recommended: 3.8+, 3.10 includes a bug that causes pyinstaller to, apparently have errors) [Python Downloads](https://www.python.org/downloads/)

> [!IMPORTANT]
> My implementation of this bot will check if your Python version is acceptable at the very start!

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
git clone https://github.com/Endlosschleifenet/roblox-starving-artists-bot
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

> [!IMPORTANT]
> The bot.py in this repository are the optimised settings for a full-screen 1920x1080 screen.

1. Start the "[Starving Artists](https://www.roblox.com/games/8916037983/starving-artists-DONATION-GAME)" game on Roblox
2. Position the game window appropriately (Fullscreen is recommended for 1920x1080 screens)

3. Run the bot by clicking on bot.py or by typing `py bot.py`

4. Follow on-screen instructions

5. If any help is required make a bug report with the tag `#assistance`

## Contributing

Feel free to change, modify, fork, edit, pull whatever! The License allows changes without need for permission or discussion. If you'd like to discuss any bugs or changes or make a pull request feel more than free!

Alternatively, reporting bugs in [Issues](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/issues) or engaging in [Discussions](https://github.com/Endlosschleifenet/roblox-starving-artists-bot/discussions) are great way to contribute. Just ensure that you are respectful and patient with others and contributors alike!

If you would like to be apart of the "official" contributors etc., please contact me with any of the contact methods below!

## Contact info

* Discord: `.replicr`
* Telegram: `https://t.me/alixsandr_a`
* Steam: `https://steamcommunity.com/profiles/76561199665164189/`

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

from ahk import AHK


ahk = AHK()

ahk.add_hotkey('^x', lambda: print(ahk.mouse_position))
ahk.start_hotkeys()
ahk.block_forever()


# Press Ctrl + X to print co-ordinates into the console

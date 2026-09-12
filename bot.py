
import pyautogui
import time
import pyperclip
from gemini_ai import ask_suvro

# Click the icon
pyautogui.click(847, 750)
time.sleep(1)

# Select the message text
pyautogui.moveTo(483, 92)
pyautogui.dragTo(1330, 642, duration=1, button="left")
time.sleep(0.5)

# Copy selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Get copied text
text = pyperclip.paste()

print("Received:", text)

# Generate Gemini response
response = ask_suvro(text)

print("Response:", response)

# Copy response to clipboard
pyperclip.copy(response)

# Click WhatsApp message box
pyautogui.click(766, 689)
time.sleep(0.5)

# Paste response
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# Send message
pyautogui.click(1331, 677)


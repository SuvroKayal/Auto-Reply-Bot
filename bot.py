import pyautogui
import time
import pyperclip
from gemini_ai import ask_suvro

def is_last_message_from_sender(chat_log):
    messages = chat_log.strip().split("] ")[-1]
    sender = messages.split(":")[0].strip()

    return sender != "Suvro"

# Click the icon once
pyautogui.click(847, 750)
time.sleep(2)


while True:

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

    # Deselect the selected text 
    pyautogui.click(483, 92) 
    time.sleep(0.5)

    # Reply only if the last message is NOT from Suvro
    if not is_last_message_from_sender(text):
        time.sleep(2)
        continue

    # Generate Gemini response
    response = ask_suvro(text)

    print("Response:", response)

    # Copy response to clipboard
    pyperclip.copy(response)

    # Click WhatsApp message box
    pyautogui.click(725, 674)
    time.sleep(0.5)

    # Paste response
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    # Send message
    pyautogui.click(1331, 677)

    time.sleep(20)
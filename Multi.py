import pyautogui
import time
import subprocess
import pyperclip

# Step 1: Launch Omnissa Horizon Client
subprocess.Popen(r"C:\Program Files\Omnissa\Omnissa Horizon Client\horizon-client.exe")
time.sleep(5)

# Step 2: Double-click the server tile
pyautogui.click(262, 194, clicks=2)
time.sleep(5)

# Step 3: Click into the username field
pyautogui.click(834, 502, clicks=2)
time.sleep(1)

# Step 4: Clear the prefilled username
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.3)
pyautogui.press('backspace')
time.sleep(0.3)

# Step 5: Paste your username
pyperclip.copy("vigneshd")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# Step 6: Move to password field
pyautogui.press('tab')
time.sleep(0.5)

# Step 7: Paste your password
pyperclip.copy("Anunta@1234567890@")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# Step 8: Login
pyautogui.press('enter')

# Step 9: Wait for VDI list to load
time.sleep(8)

# Step 10: Click the VDI
pyautogui.click(1147, 256, clicks=2)
time.sleep(30)

# Step 11: Open welcome.docx
pyautogui.press('win')
time.sleep(3)
pyautogui.write('Testdocument.docx', interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(15)

# Step 12: Print the document
pyautogui.hotkey('ctrl', 'p')
time.sleep(5)

# Step 2: Select Printer
pyautogui.click(901, 287, clicks=2)  # Coordinates for printer drop-down
time.sleep(1)

printer_image1 = r"C:\Users\Vignesh\Desktop\PY\mf427_printer.png"
location = pyautogui.locateCenterOnScreen(printer_image1, confidence=0.8)

if location:
    pyautogui.click(location)
    print("M506 Printer selected.")
else:
    print("M506 Printer not found.")
    exit()

time.sleep(3)

#Step 14: TC:1 Current Page

pyautogui.click(693, 577, clicks=1)  # Update this with the correct coordinates
time.sleep(3)
pyautogui.press('enter')

time.sleep(30)

#Step 15 TC:2 N-up

pyautogui.hotkey('ctrl', 'p')
time.sleep(3)

#Step 15.1: Set N-Up layout
# Click on the dropdown for "Pages per Sheet"
pyautogui.click(1128, 743, clicks=2)  # Adjust to correct dropdown location
time.sleep(2)

# Navigate to "2 pages per sheet"
pyautogui.press('down', presses=2, interval=0.5)  # Adjust # of presses as needed
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(20)

# Step 16: TC:3 Uncollated

pyautogui.hotkey('ctrl', 'p')
time.sleep(3)

# Step 16.1: Uncollated drop-down (adjust tabs as needed)

pyautogui.click(1194, 584, clicks=2)
time.sleep(2)
pyautogui.write("2", interval=0.1)
time.sleep(2)
pyautogui.click(1094, 641, clicks=1)
time.sleep(3)
pyautogui.press('enter')
time.sleep(20)

# Step 17: TC:4 Collated
pyautogui.hotkey('ctrl', 'p')
time.sleep(3)
pyautogui.click(1194, 584, clicks=2)
time.sleep(2)
pyautogui.write("2", interval=0.1)
time.sleep(2)
pyautogui.click(1094, 641, clicks=1)
#pyautogui.click()
time.sleep(3)
pyautogui.press('enter')
time.sleep(20)


# Test the second printer

# Step 1: Print the document
pyautogui.hotkey('ctrl', 'p')
time.sleep(1)

# Step 2: Select Printer
pyautogui.click(901, 287, clicks=2)  # Coordinates for printer drop-down
time.sleep(1)

printer_image = r"C:\Users\Vignesh\Desktop\PY\m506_printer.png"
location = pyautogui.locateCenterOnScreen(printer_image, confidence=0.8)

if location:
    pyautogui.click(location)
    print("M506 Printer selected.")
else:
    print("M506 Printer not found.")
    exit()

time.sleep(3)


#Step 3: TC:1 Current Page

pyautogui.click(693, 577, clicks=1)  # Update this with the correct coordinates
time.sleep(3)
pyautogui.press('enter')

time.sleep(20)

#Step 4 TC:2 N-up

pyautogui.hotkey('ctrl', 'p')
time.sleep(3)

#Step 4.1: Set N-Up layout
# Click on the dropdown for "Pages per Sheet"
pyautogui.click(1128, 743, clicks=2)  # Adjust to correct dropdown location
time.sleep(2)

# Navigate to "2 pages per sheet"
pyautogui.press('down', presses=2, interval=0.5)  # Adjust # of presses as needed
pyautogui.press('enter')
pyautogui.press('enter')

time.sleep(30)

# Step 5: TC:3 Uncollated

pyautogui.hotkey('ctrl', 'p')
time.sleep(3)

# Step 5.1: Uncollated drop-down (adjust tabs as needed)

pyautogui.click(1194, 584, clicks=2)
time.sleep(2)
pyautogui.write("2", interval=0.1)
time.sleep(2)
pyautogui.click(1094, 641, clicks=1)
time.sleep(3)
pyautogui.press('enter')
time.sleep(30)

# Step 6: TC:4 Collated
pyautogui.hotkey('ctrl', 'p')
time.sleep(3)
pyautogui.click(1194, 584, clicks=2)
time.sleep(2)
pyautogui.write("2", interval=0.1)
time.sleep(2)
pyautogui.click(1094, 641, clicks=1)
#pyautogui.click()
time.sleep(3)
pyautogui.press('enter')
time.sleep(30)


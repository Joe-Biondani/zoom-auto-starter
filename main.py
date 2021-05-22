import pyautogui
import subprocess
from datetime import datetime
import time

timeYouWant = "DD/MM/YY HH:MM"
# SCROLL DOWN TO THE LOOP TO CHANGE THE PASS AND ID AND/OR ADD MULTIPLE DIFFERENT ZOOMS

def join(id, password):

    # Open Zoom
    subprocess.call("C:\\Users\\YOURUSERNAME\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    print("Opened Zoom")
    
    # Find the plus button
    while True:
        join1 = pyautogui.locateOnScreen("join1.png")
        if join1 != None: # double checking it has been found already
            pyautogui.click(join1) # clicking it
            print("Clicked first join button")
            break # stopping the loop so it can continue
        else:
            # not found the plus yet so zoom must of not loaded fully
            print("Not found yet")
            time.sleep(2) # little delay so I dont crash
    
    # Find the ID input textbox
    while True:
        input1 = pyautogui.locateOnScreen("idInput.png")
        if input1 != None:
            pyautogui.click(input1)
            print("Clicked ID Input area")
            break
        else:
            print("Not found ID Input yet")
            time.sleep(2)
    
    # Actually type in the ID
    pyautogui.typewrite(id)

    # Find the blue join meeting button once ID is entered
    while True:
        join2 = pyautogui.locateOnScreen("join2.png")
        if join2 != None:
            pyautogui.click(join2)
            print("Clicked second join")
            break
        else:
            print("Not found second join yet")
            time.sleep(2)

    # Find the password input textbox
    while True:
        input2 = pyautogui.locateOnScreen("passInput.png")
        if input2 != None:
            pyautogui.click(input2)
            print("Clicked Password Input area")
            break
        else:
            print("Not found Password Input yet")
            time.sleep(2)

    # Actually type the password
    pyautogui.typewrite(password)

    # Find the last join button
    while True:
        join3 = pyautogui.locateOnScreen("join3.png")
        if join3 != None:
            pyautogui.click(join3)
            print("Clicked third join button")
            break
        else:
            print("Not found yet")
            time.sleep(2)

    # Now in the waiting room
    print("In the waiting room")
    
# Actually running the function
while True:
    # Get current time
    now = datetime.now()
    # Format the time
    current_time = (now.strftime("%d/%m/%y %H:%M"))
    # Check the time (CHANGE IT TO YOUR DESIRED TIME)
    if current_time == timeYouWant:
        # run function and stop the loop
        join("ID", "PASSWORD")
        break
    else:
        # give it a 5 sec delay before checking again
        time.sleep(5)

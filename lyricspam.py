import pyautogui
import time

print("This is a lyrics spammer script. - Why? Why not. \n Make sure you have a text field in focus. \n Be careful not to lose friends. \n Hit ^C  anytime to stop. \n")
input('Press ENTER to continue...')

# ugly way to countdown
print("Starting in 10...")
time.sleep(1)
print("Starting in 9...")
time.sleep(1)
print("Starting in 8...")
time.sleep(1)
print("Starting in 7...")
time.sleep(1)
print("Starting in 6...")
time.sleep(1)
print("Starting in 5...")
time.sleep(1)
print("Starting in 4...")
time.sleep(1)
print("Starting in 3...")
time.sleep(1)
print("Starting in 2...")
time.sleep(1)
print("Starting in 1...")
time.sleep(1)
print("Starting now... \n")

with open('lyrics.txt', 'r') as file:
    sourceFile = file.read().replace('\n', ' ')
words = sourceFile.split()

for word in words:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    print('Typing '+ word)

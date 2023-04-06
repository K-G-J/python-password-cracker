import random
import pyautogui

# python3 brute_force.py

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

allchar = list(chars)

pwd = pyautogui.password("Enter a password:")

sample_pwd = ""

while sample_pwd != pwd:
    sample_pwd = random.choices(allchar, k=len(pwd))

    print(f"<===== {str(sample_pwd)} =====>")

    if sample_pwd == list(pwd):
        print(f"The Password is : {''.join(sample_pwd)}")
        break

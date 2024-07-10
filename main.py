from clustering import get_cluster_centers
import cv2
import keyboard
import pyautogui

cnt = 0

while True:
    while True:
        if keyboard.is_pressed("2"):
            cnt = 2
            break
        if keyboard.is_pressed("3"):
            cnt = 3
            break
        if keyboard.is_pressed("4"):
            cnt = 4
            break
        if keyboard.is_pressed("5"):
            cnt = 5
            break
            
        if keyboard.is_pressed("p"):
            cnt = 0
            break
    
    if cnt == 0:
        break

    pyautogui.screenshot("scrn.png")
    
    for (x, y) in get_cluster_centers(cv2.imread("scrn.png")):
        print(x, y)
    
    while keyboard.is_pressed(str(cnt)):
        ...
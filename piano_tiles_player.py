from PIL import Image
import pygame
import os 
import autopy
import time
import math

if __name__ == '__main__':
  pygame.init()
  program_check_start = True
  program_started = False
  clicks = 10
  while program_check_start:
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          program_started = True
          program_check_start = False
        elif event.key == pygame.K_w:
          pygame.display.quit()
          pygame.quit()
          sys.exit()
  
  
  while program_started: 
    os.system("screencapture -R 518,628,400,1 -x screenshot.png")
    im = Image.open("screenshot.png")

    BLACK_TILE = (17, 17, 17, 255)
    BLOCK_CLICK_COORDS = [
      [610,628],
      [710, 628],
      [810, 628],
      [910, 628]
    ]
    def roundup(x):
      return int(math.ceil(x / 10.0)) * 10

    def click_at(x, y):
      global clicks
      autopy.mouse.move(x, y)
      print(clicks)
      print(1/roundup(clicks))
      time.sleep(0.001)
      autopy.mouse.click()
    
    if im.load()[198,1] == BLACK_TILE:
      click_at(BLOCK_CLICK_COORDS[0][0], BLOCK_CLICK_COORDS[0][1])
      clicks = clicks + 1
    elif im.load()[398,1] == BLACK_TILE:
      click_at(BLOCK_CLICK_COORDS[1][0], BLOCK_CLICK_COORDS[1][1])
      clicks = clicks + 1
    elif im.load()[598,1] == BLACK_TILE:
      click_at(BLOCK_CLICK_COORDS[2][0], BLOCK_CLICK_COORDS[2][1])
      clicks = clicks + 1
    elif im.load()[790,1] == BLACK_TILE:
      click_at(BLOCK_CLICK_COORDS[3][0], BLOCK_CLICK_COORDS[3][1])
      clicks = clicks + 1

    events = pygame.event.get()
    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          pygame.display.quit()
          pygame.quit()
          sys.exit()

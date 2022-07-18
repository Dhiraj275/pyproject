from selenium import webdriver
import pyautogui as pg
from time import sleep
#full path of chromedriver
DRIVER_PATH = 'chrome driver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
for i in range(0, 12):
    url = ('https://www.wcostream.com/high-school-dxd-hero-episode-'+str(i)+'-english-dubbed')
    driver.get(url)  # Now the target url is opened in new tab
    pg.scroll(-1100)
    pg.click(x=500, y=500)
    sleep(3)
    pg.rightClick(x=500, y=500)
    sleep(3)
    pg.click(x=600, y=600)
    sleep(4)
    pg.write(f'High School DxD S4 E{str(i)}')
    sleep(1)
    pg.press('Enter')
    sleep(60)
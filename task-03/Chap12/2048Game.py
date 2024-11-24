from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def play_2048():
    driver = webdriver.Chrome()  
    driver.get("https://gabrielecirulli.github.io/2048/")
    time.sleep(2) 


    game = driver.find_element("tag name", "html")

 
    while True:
        game.send_keys(Keys.UP)
        game.send_keys(Keys.RIGHT)
        game.send_keys(Keys.DOWN)
        game.send_keys(Keys.LEFT)

if __name__ == "__main__":
    play_2048()
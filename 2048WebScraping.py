from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def comboMove(htmlElem, moves):
    for i in range(1, moves):
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.RIGHT)


def play():
    browser = webdriver.Chrome()
    browser.get('https://play2048.co/')
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    gameStatus = browser.find_element(By.CSS_SELECTOR,'.game-container p')

    while gameStatus.text != 'Game over!':
        comboMove(htmlElem,10)
        gameStatus = browser.find_element(By.CSS_SELECTOR, '.game-container p')
    best = htmlElem.find_element(By.CLASS_NAME,"best-container").text
    print("Best Score", best)
    print("Game Over")

if __name__ == '__main__':
    play()




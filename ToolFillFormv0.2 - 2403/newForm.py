from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import Link
from variableStorage import studentPortfolioLink

# Import USERNAME & PASSWORD
from variableStorage import USERNAME, PASSWORD

#  import xpath only
from variableStorage import (
    usernameLoginBox_XPATH,
    passwordLoginBox_XPATH,
    searchBox_XPATH,
    loginButton,
)

#  Setting chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


def openLink():
    driver.get(studentPortfolioLink)


def Login(usernameXPATH, passwordXPAH):
    print("Login is running")
    driver.find_element(By.XPATH, usernameXPATH).send_keys(USERNAME)
    driver.find_element(By.XPATH, passwordXPAH).send_keys(PASSWORD)
    driver.find_element(By.XPATH, loginButton).click()
    sleep(6)
    print("Login is end")


def enableSearchBox():
    print("enable search box")
    sleep(10)
    searchBox = driver.find_element(By.XPATH, searchBox_XPATH)
    print(searchBox)
    driver.execute_script(
        "document.querySelector('.o_search_options').style.display ='block'"
    )


def main():
    openLink()
    Login(usernameLoginBox_XPATH, passwordLoginBox_XPATH)
    enableSearchBox()


main()

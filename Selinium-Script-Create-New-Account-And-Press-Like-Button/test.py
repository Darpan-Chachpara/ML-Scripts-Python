import time
from random import randint
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import concurrent.futures

def invoke_chrome():
    while True:
        chrome_options = Options()
        chrome_options.add_extension('app.crx')
        # chrome_options.add_experimental_option("debuggerAddress","localhost:9222")
        driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
        driver.implicitly_wait(5000)
        driver.get("chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/onboarding.html")
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//button[text()="Create New Wallet"]').click()
        driver.find_element_by_xpath('//button[text()="OK, I saved it somewhere"]').click()
        driver.find_element_by_xpath('//input[@name="password"]').send_keys('00000000')
        driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys('00000000')
        driver.find_element_by_xpath('//input[@type="checkbox"]').click()
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(0.4)
        driver.find_element_by_xpath('//button[text()="Continue"]').click()
        driver.find_element_by_xpath('//button[text()="Finish"]').click()
        driver.switch_to.window(driver.window_handles[0])

        driver.get('https://www.launchmynft.io/collections/32VXjKNXTHsGnJa3HxFgzwX2Mpm2RmPHXg5b7hfePGdw/6VjMoh6nUTGA4bB5KJqV')
        driver.find_element_by_xpath('//button[text()="Connect Wallet"]').click()
        driver.find_element_by_xpath('//div[@class="SignInButton_walletRow__HJGp1"]').click()
        driver.find_element_by_xpath('//button[text()="Phantom"]').click()

        main_page = driver.current_window_handle
        while True:
            try:
                print("Waiting for metamask popup, please wait...")
                time.sleep(1)
                for handle in driver.window_handles:
                    if handle != main_page:
                        login_page = handle
                driver.switch_to.window(login_page)
                break
            except Exception as wtf:
                print("metamask popup not found, retrying...")
        print(driver.current_window_handle)
        driver.find_element_by_xpath('//button[text()="Connect"]').click()

        while True:
            try:
                print("Waiting for metamask popup, please wait...")
                time.sleep(1)
                for handle in driver.window_handles:
                    if handle != main_page:
                        login_page = handle
                driver.switch_to.window(login_page)
                break
            except Exception as wtf:
                print("metamask popup not found, retrying...")
        print(driver.current_window_handle)
        driver.find_element_by_xpath('//button[text()="Approve"]').click()
        driver.switch_to.window(main_page)
        time.sleep(10)
        driver.find_element_by_xpath('//button[@class="MuiButtonBase-root css-1b47e06"]').click()
        driver.quit()

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(0 ,2):
            future = executor.submit(invoke_chrome)
main()
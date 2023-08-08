from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from setuptools import logging
from webdriver_manager. chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager




# def test_element_on_home_page():
#         service = Service(executable_path=ChromeDriverManager().install())
#         options = ChromeOptions()
#         options.add_argument("disable-infobars")
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(service=service, options=options)

@pytest.mark.page
def test_Logo():

    service = Service(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    status = driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    if status == True:
        assert True
    else:
        assert False
    driver.close()

        #
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]")))
        # title_of_page = driver.title()
        #
        # assert title_of_page == "SprintAcademy", "The title does not match the intended one"
        # print("Everything went well!")
        #
        #
        # driver.quit()
#
#
# def test_login(self):
#
#         pytest.skip()
#

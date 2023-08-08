from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager. chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
options.add_argument("disable-infobars")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://sprintacademy.co/practice")
browser.implicitly_wait(5)
input_radio1 = browser. find_element (By. ID, "radio1")
input_radio1.click()
input_radio2 = browser.find_element(By. ID, "radio2")
input_radio2.click()
input_field_example = browser.find_element(By.ID, "autocomplete")
input_field_example.click ()
input_field_example.send_keys("Hi, Farangis")
input_checkbox_exemple = browser.find_element(By. ID, "checkBoxOption1")
input_checkbox_exemple.click()
input_open_window = browser.find_element(By. ID, "openwindow")
input_open_window.click()
#---------------------------Nodir's:

driver.get('https://sprintacademy.co/practice')
driver.implicitly_wait(3)
option_first=driver.find_element(By.NAME, 'radioButton' )
option_first.click()
select_country=driver.find_element(By.ID, 'autocomplete')
select_country.send_keys('Tajikistan')
sel= Select(driver.find_element(By.NAME, 'dropdown-class-example'))
sel.select_by_visible_text("Option2")
checkbox=driver.find_element(By.NAME,'checkBoxOption3')
checkbox.click()
show=driver.find_element(By.ID, "show-textbox")
show.click()
hidebar=driver.find_element(By.ID,'hide-textbox')
hidebar.click()
name_input=driver.find_element(By.NAME,'enter-name')
name_input.send_keys('Nodir Azizov')
mouse_hover=driver.find_element(By.ID,'mousehover')
time.sleep(1)
driver.quit()
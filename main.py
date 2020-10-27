from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By




options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Visitor\\AppData\\Local\\Google\\Chrome\\User Data")


driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.maximize_window()
driver.get('https://www.fakemail.net/')
time.sleep(2)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Copy"))).click()
mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).text
time.sleep(1)
print(mail)
driver.execute_script("window.open()")
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
# driver.get('http://blinki.st/45617539b11c')         # djsamty
driver.get('http://blinki.st/cbb9fde2be7a')           # jimmy.introversy

#WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cookie-disclaimer__privacy"),"Our privacy policy"))
#driver.find_element_by_xpath("//button[@class='cookie-disclaimer__cta js-pw-link']/span[text()='Allow all cookies']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@class='button js-open-signup-popup learning-page-hero__cta']/span[text()='Start free trial']").click()
time.sleep(1)
username = driver.find_element_by_id("signup-popup_signup_email")
username.send_keys(mail)
#username.send_keys(Keys.CONTROL,'v')
password = driver.find_element_by_id("signup-popup_signup_password")
password.send_keys("StrongPass@1234")
time.sleep(1)
password.send_keys(Keys.RETURN)
time.sleep(10)
driver.switch_to.window(tabs[0])
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Refresh"))).click()
time.sleep(3)
confirm = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, r"//span[contains(text(), 'Blinkist')]")))
driver.get("https://www.fakemail.net/window/id/2")
time.sleep(2)
driver.switch_to.frame("iframeMail")
elems = driver.find_elements_by_xpath("//img[@src]")
print(elems[0].get_attribute("src"))
driver.get(elems[0].get_attribute("src"))
time.sleep(5)
# Logout
driver.get("https://www.blinkist.com/en/nc/logout")
time.sleep(3)
driver.get('https://www.fakemail.net/')
delete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Delete"))).click()
time.sleep(3)
driver.quit()





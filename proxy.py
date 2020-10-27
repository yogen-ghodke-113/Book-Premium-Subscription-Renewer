import random
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem

tor = r"C:\Users\yogen\Desktop\Tor Browser\Browser\firefox.exe"
profile = r"C:\Users\yogen\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default"
import subprocess
#subprocess.call([tor])
while True:
    driver = TorBrowserDriver("C:\\Users\\yogen\\Desktop\\Tor Browser", tor_cfg=cm.USE_STEM,tbb_profile_path=profile)

    #driver.load_url("https://check.torproject.org", wait_on_page=3, wait_for_page_body=True)

    driver.get('https://www.fakemail.net/')
    driver.execute_script("window.open()")
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.get('http://blinki.st/45617539b11c')
    driver.switch_to.window(tabs[0])
    mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).text

    print(mail)
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cookie-disclaimer__privacy"),"Our privacy policy"))
    driver.find_element_by_xpath("//button[@class='cookie-disclaimer__cta js-pw-link']/span[text()='Allow all cookies']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='button js-open-signup-popup learning-page-hero__cta']/span[text()='Start free trial']").click()
    time.sleep(1)
    username = driver.find_element_by_id("signup-popup_signup_email")
    username.send_keys(mail)
    password = driver.find_element_by_id("signup-popup_signup_password")
    password.send_keys("StrongPass@1234")
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    time.sleep(5)
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.close()
# driver.switch_to.window(tabs[0])
# time.sleep(5)
# driver.find_element_by_class_name("refresh").click()
# confirm = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "from"),"Blinkist")).click()





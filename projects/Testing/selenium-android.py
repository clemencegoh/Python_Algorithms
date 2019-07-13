from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# desired_caps = {
#     "deviceName": "Nexus 7",
#     "platformName": "Android",
#     "version" : "7.1",
#     "app": "https://testingbot.com/appium/sample.apk",
#     "realDevice": False # if you want to test on a Real Device
# }
#
# driver = webdriver.Remote("http://key:secret@hub.testingbot.com/wd/hub", desired_caps)
#
# inputA = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
# )
# inputA.send_keys("10")
#
# inputB = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputB"))
# )
# inputB.send_keys("5")
#
# sum = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "sum"))
# )
#
# if sum is not None and sum.text=="15":
#   assert True
# else:
#   assert False
#
# driver.quit()


driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
driver.get("http://google.com")
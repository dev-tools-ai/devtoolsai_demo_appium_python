from time import sleep

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver

import sys
sys.path.append('/Users/etienne/sdk/code/sdk/python-sdk')

from devtools_ai.appium import SmartDriver

# import actionchains
from selenium.webdriver.common.action_chains import ActionChains

def _main() -> None:
    caps = {
        'platformName': 'iOS',
        'allowTestPackages': True,
        'appWaitForLaunch': False,
        'newCommandTimeout': 0,
        'app': "/Users/etienne/sdk/sample_projects/devtoolsai_demo_appium_python/iosSampleApp.app",
        'automationName': 'XCUITest',
        "platformVersion": "14.4",
        "deviceName": "iPhone 12 Pro Max"
    }

    base_driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    # Convert chrome_driver to smartDriver
    driver = SmartDriver(base_driver, api_key='<<get your api key at dev-tools.ai>>')

    sleep(3)
    element = driver.find_element(by=By.XPATH, value='//XCUIElementTypeApplication[@name="iosSampleApp"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField')
    element.click();
    element.send_keys("my_username");


    element = driver.find_by_ai('ios_popup')
    element.click()

    sleep(5)
    base_driver.quit()


if __name__ == "__main__":
    _main()

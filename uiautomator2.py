from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver

from devtools_ai.appium import SmartDriver

# import actionchains
from selenium.webdriver.common.action_chains import ActionChains

def _main() -> None:
    caps = {
        'platformName': 'Android',
        'allowTestPackages': True,
        'appWaitForLaunch': False,
        'newCommandTimeout': 0,
        'app': '/Users/etienne/sdk/sample_projects/devtoolsai_demo_appium_python/todoist.apk',
    }

    base_driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    # Convert chrome_driver to smartDriver
    driver = SmartDriver(base_driver, api_key='<<get your api key at dev-tools.ai>>')

    sleep(5)
    ingest = driver.find_element(by=MobileBy.ID, value="com.todoist:id/btn_welcome_email")
    ingest.click()
    sleep(5)

    element = driver.find_by_ai("todoist_username");
    element.click()
    element.send_keys("my_username");
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    _main()

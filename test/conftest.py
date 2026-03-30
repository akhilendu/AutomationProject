
import os
from datetime import datetime

import pytest
from selenium import webdriver

from constants import constant
from utilities import screenshot


@pytest.fixture
def browzer_instance():
   driver = webdriver.Chrome()
   driver.get(constant.url)
   driver.implicitly_wait(5)
   yield driver
   driver.quit()
   
REPORT_FOLDER = None

def pytest_configure(config):
    global REPORT_FOLDER
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    REPORT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'reports', timestamp))
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    # Override the HTML report output path dynamically
    config.option.htmlpath = os.path.join(REPORT_FOLDER, "report.html")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    global REPORT_FOLDER
    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extras', [])

    if report.when in ('setup', 'call'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            safe_name = report.nodeid.replace("::", "_").replace("/", "_")
            screenshot_path = os.path.join(REPORT_FOLDER, f"{safe_name}.png")
            print(f"Capturing screenshot: {screenshot_path}")

            screenshot.capture_screenshot(item, screenshot_path)

            if os.path.exists(screenshot_path):
                html = (
                    f'<div><img src="file://{screenshot_path}" alt="screenshot" '
                    'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))

        report.extras = extra

@pytest.fixture(params=["chrome", "firefox", "edge"])
def cross_browser(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.get("https://groceryapp.uniqassosiates.com/admin/login")

    driver.maximize_window()
    yield driver


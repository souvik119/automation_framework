from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

# this will be applicable to the whole class and only executed once for the class
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10) #implicit wait
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver #pass driver to test_searchflight class TestSearchFlight
    request.cls.wait = wait #pass wait to test_searchflight class TestSearchFlight
    #above yield everything is setup
    yield
    #below yield everything is teardown
    driver.close()
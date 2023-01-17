from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class LaunchPage():
    #defines page object model for yatra landing page

    def __init__(self, driver, wait):
        self.driver = driver #connection from setup in conftest
        self.wait = wait

    def departfrom(self, departlocation):
        time.sleep(4)
        origin_city = self.driver.find_element(By.ID, "BE_flight_origin_city")
        origin_city.click()
        origin_city.send_keys(departlocation)
        origin_city.send_keys(Keys.ENTER)

    def goingto(self, goingtolocation):
        time.sleep(4)
        destination_city = self.driver.find_element(By.ID, "BE_flight_arrival_city")
        destination_city.click()
        destination_city.send_keys(goingtolocation)
        destination_city.send_keys(Keys.ENTER)

    def selectdate(self, departuredate):
        time.sleep(4)
        date_button = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        date_button.click()
        all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                time.sleep(4)
                date.click()
                break

    def clicksearch(self):
        search_button = self.driver.find_element(By.XPATH, "//input[@value='Search Flights']")
        search_button.click()
        time.sleep(4)

    
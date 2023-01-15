import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#this class gets wait and driver objects from the conftest setup method
@pytest.mark.usefixtures("setup")
class TestSearchFlight():

    def test_search_flights(self):
        
        #input origin city
        origin_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        origin_city.click()
        origin_city.send_keys("New Delhi")
        origin_city.send_keys(Keys.ENTER)

        #input destination city
        destination_city = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        destination_city.click()
        destination_city.send_keys("New York")
        destination_city.send_keys(Keys.ENTER)
import pytest
from pages.yatra_launch_page import LaunchPage #this is page object model for launch page

#this class gets wait and driver objects from the conftest setup method
@pytest.mark.usefixtures("setup")
class TestSearchFlight():

    def test_search_flights(self):
        lp = LaunchPage(self.driver, self.wait)
        #input origin city
        lp.departfrom("New Delhi")
        #input destination city
        lp.goingto("Dubai")
        #select departure date
        lp.selectdate("24/01/2023")
        #click on search button
        lp.clicksearch()
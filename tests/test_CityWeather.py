"""
Tests for checking forecasts
"""
#importing libs & Files
from pages.app_page import LoadPage

# Test to check if weather for another city is loaded
def test_weather_of_dundee_is_loaded(driver):
    #Variables
    CITY = "Dundee"

    #Initializing page
    page_load = LoadPage(driver)

    # Given forecast page is displayed
    page_load.load()

    # When City is changed to 'Dundee'
    page_load.typeCityName(CITY)

    # Then page for supplied city should be loaded
    assert page_load.getcityname() == CITY, "City should be as expected"

# Test to verify if day's data is displayed
def test_first_day_data_displayed(driver):
    # Variables
    CITY = "Dundee"

    # Initializing page
    page_load = LoadPage(driver)

    # Given forecast page is displayed for 'Dundee' city
    page_load.load()
    page_load.typeCityName(CITY)

    # When row of first day data is clicked
    page_load.clickfirstday()

    # Then day's data is expanded
    assert page_load.IsDayExpanded() == 1, "Day's data is not expanded"

    # And day's data is displayed
    assert page_load.getHoursCountOfDay() == 3

# Test to verify if day's data is collapsed
def test_first_day_data_collapsed(driver):
    # Variables
    CITY = "Dundee"

    # Initializing page
    page_load = LoadPage(driver)

    # Given forecast page is displayed for 'Dundee' city AND first day data is expanded
    page_load.load()
    page_load.typeCityName(CITY)
    page_load.clickfirstday()

    # When row of first day data is clicked again
    page_load.clickfirstday()

    # Then day's data gets collapse
    assert page_load.IsDayExpanded() == 0, "Day's data is not closed"




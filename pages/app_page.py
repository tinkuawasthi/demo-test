"""
this module is for loading and methods for the weather page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoadPage:
    #Url
    URL = "localhost:3000"
    #locators
    CITY_INPUT = (By.CSS_SELECTOR, 'input')


#Initializer
    def __init__(self,driver):
        self.driver = driver

#Methods
    def load(self):
        self.driver.get(self.URL)

    # Type city name in input box
    def typeCityName(self,test):
        city_input = self.driver.find_element(*self.CITY_INPUT)
        city_input.send_keys(Keys.CONTROL + "a",Keys.BACK_SPACE)
        city_input.send_keys(test+Keys.RETURN)

    # Click on first day element
    def clickfirstday(self):
        self.driver.find_element_by_css_selector("span[data-test*='day-1']").click()

    # Get city name value from input box
    def getcityname(self):
        city_name = self.driver.find_element(*self.CITY_INPUT).get_attribute('value')
        return city_name

    # Verify, Day's hourly data is displayed or not
    def IsDayExpanded(self):
        return len(self.driver.find_elements_by_css_selector("div[style*='max-height: 2000']"))

    # Get count of Day's hourly data
    def getHoursCountOfDay(self):
        return len(self.driver.find_elements_by_css_selector("div[style*='max-height: 2000']  span[data-test*='hour'] "))
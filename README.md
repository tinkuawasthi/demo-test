# Instructions
This repo contains the tests to verify some of the conditions of provided application made on Node.js.
App is executed on local environment and tests were also executed on the same.
The framework for testing is developed in python using pytest.
Tests are scripted in BDD approach.


# Test cases

1. test_weather_of_dundee_is_loaded 
    Scenario: New city name is entered and displayed correctly
    
        Given the Application page is displayed
        When the user enters "Dundee" for city
        Then the data gets loaded for city "Dundee"
        
    this test opens the app and then changes the city to 'Dundee' and asserts the same 
    
2. test_first_day_data_displayed 
    Scenario: weather data for first day is expanded
    
        Given the Application page is displayed for city "Dundee"
        When the user clicks on first day row
        Then the day view gets expanded
        And the hourly data gets displayed for first day
    
this test opens the first day's hourly data and asserts the same 

3. test_first_day_data_collapsed 
    Scenario: weather data for first day is collapsed
    
        Given the Application page is displayed for city "Dundee"
        And the user clicks on first day row
        And the day view is expanded
        When the user clicks on first day row again
        Then the day view gets collapsed
        
this test collapses the first day's hourly data and asserts the same 


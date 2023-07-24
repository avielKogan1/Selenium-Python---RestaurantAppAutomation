## Restaurant Rating API & UI Testing

This Python-based framework is used for conducting tests on both the API and UI of a restaurant rating application. The tests are structured in a way that they can be executed either separately or in unison.

The Selenium WebDriver is employed for UI testing and PyTest is used to structure the tests. This combination enables us to programmatically interact with UI elements, simulating the actions of an actual user, while simultaneously allowing for our tests to be organized in a manner that's scalable, maintainable, and modular.

The various functions tested in this project include fetching the top-rated restaurants, modifying a restaurant's cuisine, and adding scores to a restaurant both with and without imposing a limit.
### Getting Started

1. *Install the requirements*
   
   Install the requirements by executing pip install -r requirements.txt.
3. *Install Chrome Driver*
   
    You need to have the appropriate WebDriver installed and the path to this driver specified in your PyTest configurations (within the pytest.ini file) for Selenium to interact with the web browser for UI testing.
2. *Set your base URL*
   
   Set your base URL in the .env file.
   
3. *Set up your test data* (Optional but recommended)
   
   Specify your test data in the tests/test_data/test_data.json file.
   
4. *Configure PyTest*
   
   Update the pytest.ini file with your preferred PyTest configurations.
     
5. *Running the tests*
   
   To run the tests, use the following commands in the Makefile: sanity_tests, api_tests, sanity_tests_report, sanity_tests_headless_report, and api_tests_report.
The results from the tests will be saved in the /reports directory.

6. *Reporting*
   
    The results from the tests will be saved in the /reports directory.
 
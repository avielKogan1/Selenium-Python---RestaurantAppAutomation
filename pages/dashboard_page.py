import logging
import string
from typing import Literal

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class DashboardPage:
    URL = 'http://localhost:8080/'
    TOP_RESTAURANTS_TITLE = (By.ID, 'topRestaurantTitle')
    NUM_RESTAURANTS_INPUT_FIELD = (By.ID, 'numRestaurants')
    SUBMIT_RESTAURANTS_FORM_BUTTON = (By.ID, 'submitRestaurantsFormButton')
    TOP_RESTAURANTS_STATUS_ELEMENT = (By.ID, 'topRestaurantsStatus')
    TOP_RESTAURANTS_LIST = (By.CSS_SELECTOR, "#topRestaurantsList > li")

    RESTAURANT_NAME_INPUT_FIELD = (By.ID, 'restaurantName')
    NEW_CUISINE_INPUT_FIELD = (By.ID, 'newCuisine')
    SUBMIT_CHANGE_CUISINE_FORM_BUTTON = (By.ID, 'submitChangeCuisineFormButton')
    CHANGE_CUISINE_STATUS_ELEMENT = (By.ID, 'changeCuisineStatus')

    SCORE_TO_ADD_INPUT_FIELD = (By.ID, 'scoreToAdd')
    LIMIT_INPUT_FIELD = (By.ID, 'limit')
    SUBMIT_ADD_SCORE_FORM_BUTTON = (By.ID, 'submitAddScoreForm')
    ADD_SCORE_STATUS_ELEMENT = (By.ID, 'addScoreStatus')

    top_restaurants_success_status_text = "Status: OK"
    add_scores_success_status_text = "Status: Scores updated successfully"


    def __init__(self, driver):
        self.driver = driver
        logger.info("DashboardPage created")

    def goto(self):
        self.driver.get(self.URL)
        logger.info(f"Navigation to url: {self.URL} performed.")

    def verify_page_loaded(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.TOP_RESTAURANTS_TITLE))
            logger.info("Dashboard page loaded")
        except TimeoutException:
            raise AssertionError("TOP_RESTAURANTS_TITLE is not visible after waiting for 10 seconds.")

        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.SUBMIT_RESTAURANTS_FORM_BUTTON))
        except TimeoutException:
            raise AssertionError("SUBMIT_RESTAURANTS_FORM_BUTTON is not visible after waiting for 10 seconds.")

    # Handle Top Restaurants component
    def enter_num_restaurants(self, num):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NUM_RESTAURANTS_INPUT_FIELD)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NUM_RESTAURANTS_INPUT_FIELD)).send_keys(num)
        logger.info(f"Input {num} restaurants")
    def submit_top_restaurants_form(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUBMIT_RESTAURANTS_FORM_BUTTON)
            )
            element.click()
            logger.info("Submit Top Restaurants button clicked")
        except TimeoutException:
            raise TimeoutException(f"Element with locator {self.SUBMIT_RESTAURANTS_FORM_BUTTON} was not visible after 10 seconds")

    def verify_displayed_list(self, expected_length):
        logger.info(f"Waiting for {expected_length} elements list to be displayed")
        try:
            restaurant_list = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(self.TOP_RESTAURANTS_LIST))
        except TimeoutException:
            raise AssertionError(f"Restaurant list did not become visible within 10 seconds.")

        actual_length = len(restaurant_list)
        assert actual_length == expected_length, f"Expected {expected_length} items in the list, but found {actual_length}"
        logger.info(f"{expected_length} elements/restaurants list is displayed")

    # Handle Change Cuisine component
    def enter_restaurant_name(self, name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.RESTAURANT_NAME_INPUT_FIELD)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.RESTAURANT_NAME_INPUT_FIELD)).send_keys(name)
        logger.info(f"Restaurant name = {name} entered")

    def enter_new_cuisine(self, cuisine):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NEW_CUISINE_INPUT_FIELD)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NEW_CUISINE_INPUT_FIELD)).send_keys(cuisine)
        logger.info(f"Cuisine name = {cuisine} entered")

    def submit_change_cuisine_form(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUBMIT_CHANGE_CUISINE_FORM_BUTTON)
            )
            element.click()
            logger.info("Submit Change Cuisine button clicked")
        except TimeoutException:
            raise TimeoutException(f"Element with locator {self.SUBMIT_CHANGE_CUISINE_FORM_BUTTON} was not visible after 10 seconds")

    # Handle Add Score component
    def enter_score_to_add(self, score):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SCORE_TO_ADD_INPUT_FIELD)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SCORE_TO_ADD_INPUT_FIELD)).send_keys(score)

    def enter_limit(self, limit):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LIMIT_INPUT_FIELD)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LIMIT_INPUT_FIELD)).send_keys(limit)

    def submit_add_score_form(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUBMIT_ADD_SCORE_FORM_BUTTON)).click()
        logger.info("Submit Add Score button clicked")

    def verify_top_restaurants_status(self, status: Literal["Success", "Failure"]):
        status_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TOP_RESTAURANTS_STATUS_ELEMENT)).text
        logger.info(f"top restaurants status_message : {status_message}")
        if status == "Success":
            assert status_message == self.top_restaurants_success_status_text, "Success status message not displayed after getting top restaurants"
        else:
            assert status_message != self.top_restaurants_success_status_text, "Failure status message not displayed after getting top restaurants"

    def verify_change_cuisine_status(self, status: Literal["Success", "Failure"], restaurant_name):
        status_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHANGE_CUISINE_STATUS_ELEMENT)).text
        logger.info(f"change cuisine status_message : {status_message}")
        if status == "Success":
            assert status_message == f"Status: Cuisine of restaurant {restaurant_name} updated successfully", "Success status message not displayed after changing cuisine name"
        else:
            assert status_message != f"Status: Cuisine of restaurant {restaurant_name} updated successfully", "Failure status message not displayed after changing cuisine name"


    def verify_add_score_status(self, status: Literal["Success", "Failure"]):
        status_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ADD_SCORE_STATUS_ELEMENT)).text
        logger.info(f"change cuisine status_message : {status_message}")
        if status == "Success":
            assert status_message == self.add_scores_success_status_text, "Success status message not displayed after adding scores "
        else:
            assert status_message != self.add_scores_success_status_text, "Failure status message not displayed after adding scores"



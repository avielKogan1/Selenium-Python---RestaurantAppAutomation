import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.dashboard_page import DashboardPage

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture
def driver():
    options = Options()

    if os.getenv('HEADLESS', 'false').lower() == 'true':
        options.add_argument("--headless")
    _driver = webdriver.Chrome(options=options)
    yield _driver
    _driver.quit()

@pytest.fixture
def dashboard_page(driver):
    page = DashboardPage(driver)
    page.goto()
    yield page
    driver.quit()


def test_get_top_restaurants_with_top_value(dashboard_page, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    top_restaurants = jsondata["top_restaurants"]
    dashboard_page.verify_page_loaded()
    dashboard_page.enter_num_restaurants(top_restaurants)
    dashboard_page.submit_top_restaurants_form()
    dashboard_page.verify_displayed_list(top_restaurants)
    dashboard_page.verify_top_restaurants_status("Success")

def test_get_top_restaurant_with_default_value(dashboard_page, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    default_top_restaurants = jsondata["default_top_restaurants"]
    dashboard_page.verify_page_loaded()
    dashboard_page.submit_top_restaurants_form()
    dashboard_page.verify_displayed_list(default_top_restaurants)
    dashboard_page.verify_top_restaurants_status("Success")

def test_change_cuisine(dashboard_page, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    restaurant_name = jsondata["restaurant_name"]
    new_cuisine = jsondata["cuisine_name"]
    dashboard_page.verify_page_loaded()
    dashboard_page.enter_restaurant_name(restaurant_name)
    dashboard_page.enter_new_cuisine(new_cuisine)
    dashboard_page.submit_change_cuisine_form()
    dashboard_page.verify_change_cuisine_status("Success", restaurant_name)

def test_add_score_without_limit(dashboard_page, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    score_to_add = jsondata["score_to_add"]
    dashboard_page.verify_page_loaded()
    dashboard_page.enter_score_to_add(score_to_add)
    dashboard_page.submit_add_score_form()
    dashboard_page.verify_add_score_status("Success")

def test_add_score_with_limit(dashboard_page, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    score_to_add = jsondata["score_to_add"]
    limit = jsondata["limit"]
    dashboard_page.verify_page_loaded()
    dashboard_page.enter_score_to_add(score_to_add)
    dashboard_page.enter_limit(limit)
    dashboard_page.submit_add_score_form()
    dashboard_page.verify_add_score_status("Success")



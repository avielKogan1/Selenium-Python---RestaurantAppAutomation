import json
import pytest
from dotenv import load_dotenv
import os
import logging

from api_methods.dashboard_page_api import DashboardPageAPI

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


load_dotenv()
BASE_URL = os.getenv('BASE_URL')
logger.info(f"BASE_URL retrieved from .env = {BASE_URL}")

# Define the path to the JSON file relative to the test file
path_to_json = os.path.join(os.path.dirname(__file__), '../../api_methods/api_routes.json')

# Load your JSON file
with open(path_to_json, 'r') as file:
    api_routes = json.load(file)


@pytest.fixture
def dashboard_page_api():
    dashboard_page_api = DashboardPageAPI()
    yield dashboard_page_api

def test_get_dashboard_page(dashboard_page_api):
    response = dashboard_page_api.get_dashboard_page()
    assert response.status_code == 200


def test_get_top_restaurant_default__value(dashboard_page_api):
    response = dashboard_page_api.get_top_restaurants_default()
    data = response.json()  # convert response to Python list of dictionaries
    logger.info(f"data : {data}")
    assert response.status_code == 200
    assert len(data) == 10
    logger.info(f"Response contains {len(data)} elements")

def test_get_top_restaurants(dashboard_page_api, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    top_restaurants = jsondata["top_restaurants"]
    response = dashboard_page_api.get_top_restaurants(top_restaurants)
    data = response.json()  # convert response to Python list of dictionaries
    logger.info(f"data : {data}")
    assert response.status_code == 200
    assert len(data) == top_restaurants
    logger.info(f"Response contains {len(data)} elements")

def test_change_cuisine(dashboard_page_api, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    restaurant_name = jsondata["restaurant_name"]
    new_cuisine = jsondata["cuisine_name"]
    response = dashboard_page_api.patch_change_cuisine(restaurant_name,new_cuisine)
    assert response.status_code == 200
    assert f"Cuisine of restaurant {restaurant_name} updated successfully" in response.text, "Response message is not displayed correctly"
    logger.info(f"Response message is {response.text}")

def test_add_score_without_limit(dashboard_page_api, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    score_to_add = jsondata["score_to_add"]
    response = dashboard_page_api.patch_add_score_without_limit(score_to_add)
    assert response.status_code == 200
    assert "Scores updated successfully" in response.text, "Response message is not displayed correctly"
    logger.info(f"Response message is {response.text}")


def test_add_score_with_limit(dashboard_page_api, datafile):
    jsondata = datafile
    logger.info("Using datafile")
    score_to_add = jsondata["score_to_add"]
    limit = jsondata["limit"]
    response = dashboard_page_api.patch_add_score_with_limit(score_to_add, limit)
    assert response.status_code == 200
    assert "Scores updated successfully" in response.text, "Response message is not displayed correctly"
    logger.info(f"Response message is {response.text}")




import json
import logging
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


load_dotenv()
BASE_URL = os.getenv('BASE_URL')
logger.info(f"BASE_URL retrieved from .env = {BASE_URL}")

# Define the path to the JSON file relative to the test file
path_to_json = os.path.join(os.path.dirname(__file__), 'api_routes.json')

# Load your JSON file
with open(path_to_json, 'r') as file:
    api_routes = json.load(file)

class DashboardPageAPI:
    def __init__(self):
        pass

    def get_dashboard_page(self):
        request_url = BASE_URL + api_routes["get_dashboard_page"]
        logger.info(f"GET request to {request_url}")
        response = requests.get(request_url)
        logger.info(f"response : {response}")
        logger.info(f"response_status_code : {response.status_code}")
        return response

    def get_top_restaurants_default(self):
        request_url = BASE_URL + api_routes["get_top_restaurants"]
        logger.info(f"GET request to {request_url}")
        response = requests.get(request_url)
        logger.info(f"response : {response}")
        logger.info(f"response_status_code : {response.status_code}")
        return response

    def get_top_restaurants(self, top: int):
        request_url = BASE_URL + api_routes["get_top_restaurants"] + f"?top={top}"
        logger.info(f"GET request to {request_url}")
        response = requests.get(request_url)
        logger.info(f"response : {response}")
        logger.info(f"response_status_code : {response.status_code}")
        return response

    def patch_change_cuisine(self, restaurant_name, cuisine_name):
        request_url = BASE_URL + api_routes["get_top_restaurants"] + f"/{restaurant_name}"
        headers = {'Content-Type': 'application/json'}
        data = {'cuisine': cuisine_name}
        logger.info(f"PATCH request to {request_url}")
        logger.info(f"Request data = {data}")
        response = requests.patch(request_url,headers=headers,data=json.dumps(data))
        logger.info(f"response : {response}")
        logger.info(f"response_status_code : {response.status_code}")
        return response


    def patch_add_score_without_limit(self, score_to_add: int):
        request_url = BASE_URL + api_routes["patch_add_score"]
        headers = {'Content-Type': 'application/json'}
        data = {'number' : score_to_add}
        logger.info(f"PATCH request to {request_url}")
        logger.info(f"Request data = {data}")
        response = requests.patch(request_url, headers=headers, data=json.dumps(data))
        logger.info(f"response : {response}")
        logger.info(f"response_status_code : {response.status_code}")
        return response

    def patch_add_score_with_limit(self, score_to_add: int, limit: int):
        request_url = BASE_URL + api_routes["patch_add_score"]
        headers = {'Content-Type': 'application/json'}
        data = {'number' : score_to_add, 'limit' : limit}
        logger.info(f"PATCH request to {request_url}")
        logger.info(f"Request data = {data}")
        response = requests.patch(request_url, headers=headers, data=json.dumps(data))
        logger.info(f"response : {response}")
        logger.info(f"response_status_code : {response.status_code}")
        return response




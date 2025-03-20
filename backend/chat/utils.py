import json

import requests
from dotenv import load_dotenv
import os

load_dotenv()


def generate_serpapi_params(query, location):
    return {
        "q": query,
        "location": location or "egypt",
        "api_key": os.getenv("SERP_API_KEY")
    }



def get_product_link(serpapi_product_link):
    session = requests.Session()
    cookies = {"api_key": os.getenv("SERP_API_KEY") , "_SerpAPI_session" : os.getenv("SERP_API_SESSION")}

    response = requests.get(serpapi_product_link , cookies=cookies)

    direct_link = response.json()["sellers_results"]["online_sellers"][0]["direct_link"]
    print(direct_link)

    return direct_link
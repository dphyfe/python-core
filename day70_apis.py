# Day 70: working with APIs for my practice

import json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def my_get_data(url):
    try:
        with urlopen(url) as response:
            my_data = response.read()
            return json.loads(my_data)
    except HTTPError as e:
        print(f"My HTTP error: {e.code}")
    except URLError as e:
        print(f"My URL error: {e.reason}")

print("My API function defined")

def my_post_data(url, data):
    my_json_data = json.dumps(data).encode('utf-8')
    my_req = Request(url, data=my_json_data, method='POST')
    my_req.add_header('Content-Type', 'application/json')
    try:
        with urlopen(my_req) as response:
            return json.loads(response.read())
    except Exception as e:
        print(f"My error: {e}")

print("My POST function defined")

def my_api_with_headers(url, headers):
    my_req = Request(url)
    for key, value in headers.items():
        my_req.add_header(key, value)
    try:
        with urlopen(my_req) as response:
            return json.loads(response.read())
    except Exception as e:
        print(f"My error: {e}")

print("My headers function defined")

my_example_response = {
    "users": [
        {"name": "David", "age": 30},
        {"name": "Taylor", "age": 28}
    ],
    "count": 2
}

print(f"My example response: {json.dumps(my_example_response, indent=2)}")

def my_parse_response(response):
    if isinstance(response, dict):
        my_users = response.get("users", [])
        print(f"My found {len(my_users)} users")
        for my_user in my_users:
            print(f"My user: {my_user['name']}, age {my_user['age']}")

my_parse_response(my_example_response)

my_api_data = {"endpoint": "https://api.example.com", "key": "my-api-key"}
print(f"My API config: {my_api_data}")

print("My API examples complete")

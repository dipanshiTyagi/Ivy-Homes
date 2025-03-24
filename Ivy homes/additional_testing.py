import requests
import time

# Base URL of the API
BASE_URL = "http://35.200.185.69:8000/v4"

# Test the autocomplete endpoint
def test_autocomplete(query):
    url = f"{BASE_URL}/autocomplete"
    params = {"query": query}
    response = requests.get(url, params=params)
    
    print(f"Testing autocomplete with query: '{query}'")
    print(f"Request URL: {response.url}")
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.json()}\n")

# Test other possible endpoints
def test_endpoint(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    
    print(f"Testing endpoint: '{endpoint}'")
    print(f"Request URL: {response.url}")
    print(f"Response Status: {response.status_code}")
    print(f"Response Body: {response.json()}\n")

# Test rate limiting
def test_rate_limiting():
    print("Testing rate limiting...")
    for i in range(15):  # Send 15 requests in quick succession
        response = requests.get(f"{BASE_URL}/autocomplete", params={"query": "a"})
        print(f"Request {i + 1}: Status Code = {response.status_code}")
        time.sleep(1)  # Add a 1-second delay between requests

# Test input validation
def test_input_validation():
    test_cases = [
        "",  # Empty query
        " ",  # Space
        "123",  # Numbers
        "!@#$%",  # Special characters
        "你好",  # Non-English characters
        "a" * 1000,  # Very long string
    ]
    
    for query in test_cases:
        test_autocomplete(query)
        time.sleep(1)  # Add a 1-second delay between requests

# Main function to explore the API
def explore_api():
    # Test the autocomplete endpoint
    test_autocomplete("a")
    test_autocomplete("aa")
    test_autocomplete("invalid")

    # Test other possible endpoints
    endpoints = ["search", "list", "details", "metadata"]
    for endpoint in endpoints:
        test_endpoint(endpoint)
        time.sleep(1)  # Add a 1-second delay between requests

    # Test rate limiting
    test_rate_limiting()

    # Test input validation
    test_input_validation()

if __name__ == "__main__":
    explore_api()
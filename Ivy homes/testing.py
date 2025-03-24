# import requests

# BASE_URL = "http://35.200.185.69:8000/v1/autocomplete"

# def test_api(query):
#     """Sends a request to the API and prints the response."""
#     response = requests.get(BASE_URL, params={"query": query})
#     if response.status_code == 200:
#         print(response.json())  # Print the list of names
#     else:
#         print(f"Error {response.status_code}: {response.text}")

# # Try different queries
# test_api("A")  # Test with letter A
# test_api("B")  # Test with letter B
# test_api("Al")  # Test with a two-letter prefix
# test_api("")   # Test with an empty query (maybe returns 



# import requests
# import json

# BASE_URL = "http://35.200.185.69:8000/v1/autocomplete"

# def test_api(query):
#     """Sends a request to the API and returns the response."""
#     response = requests.get(BASE_URL, params={"query": query})
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": f"Error {response.status_code}: {response.text}"}

# def log_results(label, query, response):
#     """Logs the test case results."""
#     print(f"\n🔹 {label} | Query: '{query}'")
#     print(json.dumps(response, indent=4))

# def run_tests():
#     print("🚀 Running API Behavior Tests...\n")

#     # Test 1: Single-letter input
#     log_results("Single-letter Query", "A", test_api("A"))
#     log_results("Single-letter Query", "a", test_api("a"))

#     # Test 2: Two-letter input
#     log_results("Two-letter Query", "aa", test_api("aa"))
#     log_results("Two-letter Query", "Ab", test_api("Ab"))

#     # Test 3: Three-letter input
#     log_results("Three-letter Query", "aaa", test_api("aaa"))
#     log_results("Three-letter Query", "Aaa", test_api("Aaa"))

#     # Test 4: Case sensitivity
#     log_results("Lowercase Query", "ab", test_api("ab"))
#     log_results("Uppercase Query", "AB", test_api("AB"))

#     # Test 5: Empty input behavior
#     log_results("Empty Query", "", test_api(""))
#     log_results("Empty Query", "", test_api(""))

#     # Test 6: Maximum results check (ensuring it's capped at 10)
#     log_results("Max Results", "a", test_api("a"))

#     # Test 7: Checking different prefix lengths
#     log_results("Prefix Query", "aab", test_api("aab"))
#     log_results("Prefix Query", "aac", test_api("aac"))
#     log_results("Prefix Query", "aad", test_api("aad"))
#     log_results("Prefix Query", "b", test_api("bb"))
#     log_results("Prefix Query", "abcd", test_api("aabb"))

#     # Test 8: Checking consistency of results
#     result1 = test_api("aa")
#     result2 = test_api("aa")
#     log_results("Consistency Check", "aa", {"consistent": result1 == result2})


#     #Test 9: Checking special characters result
#     log_results("Special-letter Query", "#", test_api("#"))
#     log_results("Special-letter Query", "@", test_api("@"))

# if __name__ == "__main__":
#     run_tests()



import requests
import json
import time
import string

BASE_URL = "http://35.200.185.69:8000/v3/autocomplete"

def test_api(query):
    """Sends a request to the API and returns the response."""
    try:
        response = requests.get(BASE_URL, params={"query": query}, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def log_results(label, query, response):
    """Logs the test case results."""
    print(f"\n🔹 {label} | Query: '{query}'")
    print(json.dumps(response, indent=4))

def explore_pagination():
    """Tests if there's a way to retrieve more results beyond a limit."""
    log_results("Pagination Check", "a", test_api("a"))

def explore_rate_limiting():
    """Sends rapid requests to check for rate limiting behavior."""
    print("\n🚀 Testing rate limits...")
    for i in range(15):  # Sending 15 rapid requests
        response = test_api("test")
        print(f"Request {i+1}: {response}")
        time.sleep(0.5)  # Adjust this delay to test limits

def explore_special_inputs():
    """Tests numbers, symbols, spaces, and non-English characters."""
    special_inputs = ["123", "#$%", " ", "हेलो", "你好", "مرحبا", "<script>alert('xss')</script>", "' OR 1=1 --"]
    for query in special_inputs:
        log_results("Special Input", query, test_api(query))

def explore_fuzzy_matching():
    """Tests if the API can handle typos and partial matches."""
    fuzzy_tests = ["grame", "grm", "garmnt", "grmnts"]  # Variants of "garment"
    for query in fuzzy_tests:
        log_results("Fuzzy Match", query, test_api(query))

def explore_case_sensitivity():
    """Tests if API results change based on capitalization."""
    cases = ["apple", "Apple", "APPLE"]
    for query in cases:
        log_results("Case Sensitivity", query, test_api(query))

def explore_character_set():
    """Tests all possible ASCII characters."""
    for char in string.ascii_letters + string.digits + string.punctuation + " ":
        log_results("Character Test", char, test_api(char))

def run_tests():
    print("🚀 Running API Exploration Tests...\n")

    # Basic tests from previous script
    log_results("Single-letter Query", "A", test_api("A"))
    log_results("Two-letter Query", "Al", test_api("Al"))

    # Advanced exploration
    explore_pagination()
    explore_rate_limiting()
    explore_special_inputs()
    explore_fuzzy_matching()
    explore_case_sensitivity()
    explore_character_set()

if __name__ == "__main__":
    run_tests()


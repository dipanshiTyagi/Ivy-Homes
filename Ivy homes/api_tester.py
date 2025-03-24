# import requests
# import time
# from collections import deque

# # Base URL of the API
# API_URL = "http://35.200.185.69:8000/v1/autocomplete"

# # Global variables to store results and track progress
# results = set()
# queue = deque()
# processed_prefixes = set()
# rate_limit_delay = 1  # Delay in seconds to avoid rate limiting

# def query_api(prefix):
#     """
#     Query the API with a given prefix and return the results.
#     """
#     try:
#         params = {"query": prefix}
#         response = requests.get(API_URL, params=params)
        
#         # Debugging: Print the full request URL and response
#         print(f"Request URL: {response.url}")
#         print(f"Response Status: {response.status_code}")
#         print(f"Response Body: {response.text}")

#         if response.status_code == 200:
#             data = response.json()
#             return data.get("results", [])
#         else:
#             print(f"Error: {response.status_code} for prefix '{prefix}'")
#             return []
#     except Exception as e:
#         print(f"Exception for prefix '{prefix}': {e}")
#         return []

# def extract_names():
#     """
#     Extract all possible names using a BFS approach.
#     """
#     # Start with lowercase letters (based on API behavior)
#     for char in "abcdefghijklmnopqrstuvwxyz":
#         queue.append(char)

#     while queue:
#         prefix = queue.popleft()

#         # Skip if the prefix has already been processed
#         if prefix in processed_prefixes:
#             continue
#         processed_prefixes.add(prefix)

#         # Query the API
#         names = query_api(prefix)

#         for name in names:
#             if name not in results:
#                 results.add(name)
#                 print(f"Found: {name}")

#                 # Add new prefixes to the queue for further exploration
#                 if len(name) > len(prefix):
#                     new_prefix = name[:len(prefix) + 1]
#                     queue.append(new_prefix)

#         # Respect rate limits
#         time.sleep(rate_limit_delay)

#     print("Extraction complete.")

# if __name__ == "__main__":
#     extract_names()
#     print(f"Total names extracted: {len(results)}")


import requests
import time
from collections import deque

# Base URL of the API
API_URL = "http://35.200.185.69:8000/v3/autocomplete"

# Global variables to store results and track progress
results = set()
queue = deque()
processed_prefixes = set()
rate_limit_delay = 1  # Delay in seconds to avoid rate limiting

def query_api(prefix):
    """
    Query the API with a given prefix and return the results.
    """
    try:
        params = {"query": prefix}
        response = requests.get(API_URL, params=params)
        
        # Debugging: Print the full request URL and response
        print(f"Request URL: {response.url}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        else:
            print(f"Error: {response.status_code} for prefix '{prefix}'")
            return []
    except Exception as e:
        print(f"Exception for prefix '{prefix}': {e}")
        return []

def extract_names():
    """
    Extract all possible names using a BFS approach.
    """
    # Start with lowercase letters (based on API behavior)
    for char in "abcdefghijklmnopqrstuvwxyz":
        queue.append(char)

    while queue:
        prefix = queue.popleft()

        # Skip if the prefix has already been processed
        if prefix in processed_prefixes:
            continue
        processed_prefixes.add(prefix)

        # Query the API
        names = query_api(prefix)

        for name in names:
            if name not in results:
                results.add(name)
                print(f"Found: {name}")

                # Add new prefixes to the queue for further exploration
                if len(name) > len(prefix):
                    new_prefix = name[:len(prefix) + 1]
                    queue.append(new_prefix)

        # Respect rate limits
        time.sleep(rate_limit_delay)

    print("Extraction complete.")

if __name__ == "__main__":
    extract_names()
    print(f"Total names extracted: {len(results)}")
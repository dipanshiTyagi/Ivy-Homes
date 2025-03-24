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

# Tracking counters
total_requests = 0
total_records = 0

def query_api(prefix):
    """
    Query the API with a given prefix and return the results.
    """
    global total_requests, total_records  # Use global counters
    try:
        params = {"query": prefix}
        response = requests.get(API_URL, params=params)
        
        total_requests += 1  # Increment request counter

        if response.status_code == 200:
            data = response.json()
            names = data.get("results", [])
            total_records += len(names)  # Count retrieved records
            return names
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
    for char in "abcdefghijklmnopqrstuvwxyz":
        queue.append(char)

    while queue:
        prefix = queue.popleft()

        if prefix in processed_prefixes:
            continue
        processed_prefixes.add(prefix)

        names = query_api(prefix)

        for name in names:
            if name not in results:
                results.add(name)
                print(f"Found: {name}")

                if len(name) > len(prefix):
                    new_prefix = name[:len(prefix) + 1]
                    queue.append(new_prefix)

        time.sleep(rate_limit_delay)  # Avoid rate-limiting

    print("Extraction complete.")

if __name__ == "__main__":
    extract_names()
    print(f"Total requests made: {total_requests}")
    print(f"Total records retrieved: {total_records}")

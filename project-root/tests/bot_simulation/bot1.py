import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def simulate_bot():
    session = requests.Session()
    url = "http://127.0.0.1:8000/"

    try:
        response = session.get(url)
        response.raise_for_status()  # Raises an error for HTTP codes 4xx/5xx
        return response.text
    except ConnectionError:
        print("Failed to connect to the server. Ensure the server is running and the URL is correct.")
    except Timeout:
        print("The request timed out. Try again later.")
    except TooManyRedirects:
        print("Too many redirects. Check the URL.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(simulate_bot())

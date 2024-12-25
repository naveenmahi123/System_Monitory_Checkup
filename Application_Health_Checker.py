import requests
import logging

# Setup logging
logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Application URL
APPLICATION_URL = "http://example.com"

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logging.info(f"Application is UP. Status code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    check_application_health(APPLICATION_URL)

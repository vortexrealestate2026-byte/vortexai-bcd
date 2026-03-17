import requests
import logging

logger = logging.getLogger("vortex-ai")


def get_vehicles():

    url = "https://api.api-ninjas.com/v1/cars?limit=10"

    headers = {
        "X-Api-Key": "YOUR_API_KEY"
    }

    try:

        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            return r.json()

    except Exception as e:
        logger.error(f"Vehicle API error: {e}")

    return []

import os
import requests
from dotenv import load_dotenv


load_dotenv()
HASDATA_API_KEY = os.getenv('HASDATA_API_KEY')

URL = 'https://api.hasdata.com/scrape/google/serp'

HEADERS = {
    'x-api-key': HASDATA_API_KEY,
    'Content-Type': "application/json"
}


def get_data(q: str, at_page: int = 0) -> dict:
    if not HASDATA_API_KEY:
        raise RuntimeError(
            "Missing HasData API key. Set HASDATA_API_KEY in your .env file."
        )
    if at_page < 0:
        raise ValueError("at_page must be >= 0")

    params = {
        "q": q,
        "start": at_page,
    }
    response = requests.get(url=URL, params=params, headers=HEADERS, timeout=30)
    response.raise_for_status()

    try:
        return response.json()
    except ValueError as exc:
        raise RuntimeError(f"Invalid JSON from HasData API") from exc


import os
import json
from urllib.parse import urlparse


def read_domain_data(domain: str):
    file_name = f'{domain}.json'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'output', file_name)

    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        json_data = json.load(f)
        return json_data


def write_domain_data(domain: str, new_data: dict):
    file_name = f'{domain}.json'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'output', file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(new_data, f, indent=4)


def read_lines_from_settings_txt(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'settings', file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def clean_domain(url: str) -> str:
    if "://" not in url:
        url = "http://" + url  # helps urlparse work properly

    domain = urlparse(url).netloc
    domain = domain.removeprefix("www.")

    return domain
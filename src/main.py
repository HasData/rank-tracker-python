import api
import time
from datetime import datetime
from visualization import make_graph, make_excel_report
from utils import read_domain_data, read_lines_from_settings_txt, write_domain_data, clean_domain


def get_rank(query: str, target_domain: str):
    max_pages_search = 10

    for page_idx in range(max_pages_search):
        data = api.get_data(query, at_page=page_idx * 10)

        if 'organicResults' not in data:
            return None

        for result_idx, result in enumerate(data['organicResults']):
            domain_normalized = clean_domain(result.get('link', ''))
            if domain_normalized == target_domain:
                search_rank = page_idx * 10 + result.get('position', result_idx + 1)
                return search_rank

    return None


def main():
    lines = read_lines_from_settings_txt('target_domain.txt')
    if not lines:
        raise RuntimeError("Missing target domain in --- settings/target_domain.txt")
    target_domain = clean_domain(lines[0])
    if not target_domain:
        raise RuntimeError("Missing target domain in --- settings/target_domain.txt")

    queries = read_lines_from_settings_txt('search_queries.txt')
    if not queries:
        raise RuntimeError("Missing queries in --- settings/search_queries.txt")

    domain_data = read_domain_data(target_domain)
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not domain_data:
        domain_data = {target_domain: {}}

    for query in queries:
        if query not in domain_data[target_domain]:
            domain_data[target_domain][query] = []

        try:
            rank = get_rank(query, target_domain)
        except Exception as e:
            print(f'Error fetching rank for "{query}": {e}')
            rank = None
        domain_data[target_domain][query].append([datetime_now, rank])

    write_domain_data(target_domain, domain_data)
    make_graph(target_domain, domain_data)
    make_excel_report(target_domain, domain_data)
    print('Files saved successfully\n')


if __name__ == '__main__':

    days_to_wait = 0
    hours_to_wait = 4
    minutes_to_wait = 0
    seconds_to_wait = 0

    total_time_to_wait = (days_to_wait*86400) + (hours_to_wait*3600) + (minutes_to_wait*60) + seconds_to_wait

    while True:
        try:
            main()
        except Exception as e:
            print(f'Error during execution: {e}')
        time.sleep(total_time_to_wait)

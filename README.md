![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Requests](https://img.shields.io/badge/requests-enabled-2ea44f)
![dotenv](https://img.shields.io/badge/config-.env-orange)

# SEO Rank Tracker
[![HasData_bannner](assets/banner.png)](https://hasdata.com/?utm_source=github&utm_medium=repo&utm_campaign=rank-tracker-python)

Companion code for a YouTube video showing how to track your website SEO rank with [HasData Google SERP API](https://hasdata.com/apis/google-serp-api?utm_source=github&utm_medium=repo&utm_campaign=rank-tracker-python).

> Lightweight tutorial project: query Google SERP data, extract LinkedIn profiles, emails, location etc. From search results, and rank the best match for a person.

[![Watch the video](assets/youtube-preview.png)](https://youtu.be/s0yGUf02IrQ)

This repository runs main.py to do the following:

- Read the settings files, where user inputs desired queries and domain to target
- Uses HasData Google SERP API to find the rank for the specified domain and queries.
- Saves the results in the repo output folder with these formats: JSON, EXCEL, Graph Image PNG  
- Repeats this process every 4h to update the data.

## Quick Start

```bash
pip install -r requirements.txt
```

Create `.env`
```env
HASDATA_API_KEY=your_api_key_here
```

Run the batch example:

```bash
python src/main.py
```


## Workflow

```text
Read Input from Settings folder
       |
       v
Scrape the rank of the domain for specified queries
       |
       v
Save results in output/
       |
       v
Repeat every 4h
```

## Project Structure

```text
extract-emails-from-google-search/
|-- assets/
    |-- banner.png
    |-- youtube-preview.png
|-- output/
    |-- example.com.json
    |-- example.com.png
    |-- example.com.xlsx
|-- output/
    |-- search_queries.txt
    |-- target_domain.txt
|-- src/
    |-- __init__.py 
    |-- api.py 
    |-- main.py 
    |-- utils.py 
    |-- visualization.py 
|-- .env
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
```

## Requirements

- Python 3.10+
- A HasData API key

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create `.env` in the project root,
```env
HASDATA_API_KEY=your_api_key_here
```

The scripts load this variable automatically with `python-dotenv`.


## Scripts

Run
---
### `src/main.py`


## Notes

- Results depend on what Google snippets expose at request time.
- This approach only finds domains that appear publicly in search results.
- Google tends to not give the same results for the same search query everytime.
- API usage depends on your HasData account and quota.

## Why This Repo Exists

This project is meant to be extra material for a YouTube tutorial, so the code stays small, readable, and easy to follow. The focus is on demonstrating the core idea clearly rather than building a production-grade pipeline.

## Use Cases

- PR research
- Market research
- tutorial material for scraping and SERP parsing
- Business performance tracking

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
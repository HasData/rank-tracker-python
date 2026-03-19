![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Requests](https://img.shields.io/badge/requests-enabled-2ea44f)
![dotenv](https://img.shields.io/badge/config-.env-orange)

# Draft 2
[![HasData_bannner](assets/banner.png)](https://hasdata.com/?utm_source=github&utm_medium=repo&utm_campaign=extract-emails-from-google-search)

Companion code for a YouTube video showing how to find publicly visible LinkedIn profiles from Google search with the [HasData Google SERP API](https://hasdata.com/apis/google-serp-api?utm_source=github&utm_medium=repo&utm_campaign=extract-emails-from-google-search).

> Lightweight tutorial project: query Google SERP data, extract LinkedIn profiles, emails, location etc. From search results, and rank the best match for a person.

[![Watch the video](assets/youtube-preview.png)](https://youtu.be/s0yGUf02IrQ)

This repository includes small Python examples for:

- Scraping LinkedIn profiles of people with the given Industry, Job Title and Location
- Extracting info like full name, location, job title etc. From a given file of profiles with the help of AI.
- Extracting the email of every person in a given file.
- Extracting company information given a file that include a list of company names, With the help of AI

## Quick Start

```bash
pip install -r requirements.txt
```

Create `.env`
use LLM_SITE is only if you're using an LLM aggregator
```env
HASDATA_API_KEY=your_api_key_here
LLM_KEY=your_llm_key_here
LLM_SITE=your_llm_site_here
```

Run the batch example:

```bash
python src/example_1.py
```


## Workflow

```text
Scrape LinkedIn profiles of people with Google SERP 
       |
       v
Inference those profiles with AI to extract names, location, followers, company they work on, etc. Automatically
       |
       v
From the AI extractions we can use the name and Google SERP api with the keyword "email" to enrich the data with emails
       |
       v
From the AI extracted company names we can use Google SERP api to get more info on the company.
       |
       v
Save all the information and all the steps in JSON and CSV files.
```

## Project Structure

```text
extract-emails-from-google-search/
|-- assets/
    |-- banner.png
    |-- youtube-preview.png
|-- output/
|-- src/
    |-- __init__.py 
    |-- api.py 
    |-- example_1.py 
    |-- example_2.py 
    |-- example_3.py 
    |-- example_4.py 
    |-- llm.py 
    |-- utils.py 
|-- .env
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
```

## Requirements

- Python 3.10+
- A HasData API key
- A LLM API key

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create `.env` in the project root,
LLM_SITE is only if you're using an LLM aggregator
```env
HASDATA_API_KEY=your_api_key_here
LLM_KEY=your_llm_key_here
LLM_SITE=your_llm_site_here
```

The scripts load this variable automatically with `python-dotenv`.


## Scripts

---
### `src/example_1.py`

The simplest example. It:

1. uses HasData Google SERP to search LinkedIn profiles.
2. scans 50 pages per query.
3. outputs a file in `output/`

Run:


```bash
python src/example_1.py
```
---
### `src/example_2.py`

Single-person matching mode. It:

1. reads the data from `output/n`
2. uses LLM to understand the search results
3. extracts full name, company name, location, job title etc.
4. outputs a file in `output/`

Run:

```bash
python src/example_2.py
```
---
### `src/example_3.py`

Batch mode for multiple people from CSV. It:

1. reads the data from `output/`
2. uses HasData Google SERP api to search emails
3. finds the best matching email with confidence score
4. outputs a file with update info in `output/`

Run:

```bash
python src/example_3.py
```
---
### `src/example_4.py`

Batch mode for multiple people from CSV. It:

1. reads the data from `output/`
2. searches the companies the LLM found from LinkedIn profiles
3. using a LLM extracts company ceo, headquarters, industry involved, etc.
4. outputs a file with update info in `output/`

Run:

```bash
python src/example_4.py
```
---


## Notes

- Results depend on what Google snippets expose at request time.
- This approach only finds emails that appear publicly in search snippets.
- Accuracy is limited when multiple people share similar names.
- There's a small chance the LLM might hallucinate.
- API usage depends on your HasData account and quota.

## Why This Repo Exists

This project is meant to be extra material for a YouTube tutorial, so the code stays small, readable, and easy to follow. The focus is on demonstrating the core idea clearly rather than building a production-grade pipeline.

## Use Cases

- lead research demos
- enrichment experiments
- tutorial material for scraping and SERP parsing
- lightweight prospecting workflows

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
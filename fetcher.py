import requests
import logging
from pubmed_papers.utils import extract_company_authors

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_papers(query: str, max_results: int = 10) -> list:
    """Fetches papers from PubMed API based on the query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
    }

    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    if not paper_ids:
        logging.warning("No papers found for the query.")
        return []

    return fetch_paper_details(paper_ids)


import json

def fetch_paper_details(paper_ids: list) -> list:
    """Fetches detailed information for given paper IDs."""
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json",
    }

    response = requests.get(FETCH_URL, params=params)
    response.raise_for_status()
    data = response.json()

    # 🔥 Debug: Print the full API response
    print(json.dumps(data, indent=4))  # Pretty-print JSON response

    results = []
    for paper_id in paper_ids:
        paper_data = data["result"].get(paper_id, {})
        if paper_data:
            results.append({
                "PubmedID": paper_id,
                "Title": paper_data.get("title", "N/A"),
                "Publication Date": paper_data.get("pubdate", "N/A"),
                "Authors": paper_data.get("authors", []),
            })

    return results

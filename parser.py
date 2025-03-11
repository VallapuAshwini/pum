import re
from pubmed_papers.config import COMPANY_KEYWORDS, ACADEMIC_KEYWORDS

import re


def extract_email(paper: dict) -> str:
    """Extracts the corresponding author's email from PubMed metadata."""
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    for author in paper.get("Authors", []):
        if "@" in author.get("affiliation", ""):
            email_match = re.search(email_pattern, author["affiliation"])
            if email_match:
                return email_match.group(0)

    return "N/A"


def extract_relevant_data(papers: list) -> list:
    """Extracts and filters paper data, keeping only non-academic authors."""
    extracted_papers = []

    for paper in papers:
        non_academic_authors = []
        company_affiliations = []

        for author in paper.get("Authors", []):
            affiliation = author.get("affiliation", "").lower()

            # Check if author is company-affiliated
            if any(word in affiliation for word in COMPANY_KEYWORDS) and \
               not any(word in affiliation for word in ACADEMIC_KEYWORDS):
                non_academic_authors.append(author.get("name", "Unknown"))
                company_affiliations.append(affiliation)

        # Only save papers with at least one non-academic author
        if non_academic_authors:
            extracted_papers.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(set(company_affiliations)),
                "Corresponding Author Email": extract_email(paper)
            })

    return extracted_papers

import re

def extract_company_authors(papers: list) -> list:
    """Filters authors affiliated with pharmaceutical or biotech companies."""
    company_keywords = ["pharma", "biotech", "laboratories", "inc", "ltd", "gmbh"]

    for paper in papers:
        non_academic_authors = []
        company_affiliations = []

        for author in paper["Authors"]:
            affiliation = author.get("affiliation", "").lower()
            if any(word in affiliation for word in company_keywords):
                non_academic_authors.append(author.get("name", "Unknown"))
                company_affiliations.append(affiliation)

        paper["Non-academic Author(s)"] = ", ".join(non_academic_authors)
        paper["Company Affiliation(s)"] = ", ".join(set(company_affiliations))

    return papers

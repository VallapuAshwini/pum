# API URLs
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# API Key (Optional: Set if you have one)
API_KEY = None  # Replace with your API key

# Default search parameters
DEFAULT_MAX_RESULTS = 10

# Filtering heuristics for identifying company-affiliated authors
COMPANY_KEYWORDS = ["pharma", "biotech", "laboratories", "inc", "ltd", "gmbh"]
ACADEMIC_KEYWORDS = ["university", "college", "institute", "school", "academy"]

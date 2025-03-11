# PubMed Papers Fetcher

## 📌 Overview
`pubmed_papers` is a Python package that allows users to fetch research papers from PubMed based on a given query. It interacts with the **NCBI Entrez API** to retrieve paper details such as title, authors, and publication date.

## 🚀 Features
- Fetches research papers from PubMed using a query.
- Retrieves details such as **PubMed ID, title, authors, and publication date**.
- Supports **JSON output** for easy integration with other applications.

---

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/pubmed_papers.git
cd pubmed_papers
```

### 2️⃣ Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
.venv\Scripts\activate   # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -e .
```

---

## 📌 Usage
### 🔹 Run the Command-Line Interface (CLI)
To search for papers on **cancer treatment**, run:
```bash
python -m pubmed_papers.cli "cancer treatment"
```

### 🔹 Fetch Papers Programmatically
```python
from pubmed_papers.fetcher import fetch_papers

query = "cancer treatment"
results = fetch_papers(query)

for paper in results:
    print(f"Title: {paper['Title']}")
    print(f"Authors: {', '.join([author['name'] for author in paper['Authors']])}")
    print(f"Publication Date: {paper['Publication Date']}")
    print("-" * 50)
```

---

## ⚡ API Details
### 1️⃣ **Fetching Papers from PubMed**
The function `fetch_papers(query, max_results=10)` sends a request to the PubMed API and retrieves paper details.
```python
def fetch_papers(query: str, max_results: int = 10) -> list:
    """Fetches papers from PubMed API based on the query."""
```
### 2️⃣ **Fetching Paper Details by ID**
```python
def fetch_paper_details(paper_ids: list) -> list:
    """Fetches detailed information for given paper IDs."""
```

---

## 🛠 Troubleshooting
### 🔹 **ImportError: Cannot import name 'fetch_papers'**
✔ **Solution:** Ensure your virtual environment is activated and package is installed:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate   # Windows
pip install -e .
```

### 🔹 **No Papers Found for Query**
✔ **Solution:** Try using broader search terms.

### 🔹 **Incorrect Output Formatting**
✔ **Solution:** Use `json.dumps(results, indent=4)` to pretty-print JSON output.

---

## 📜 License
This project is licensed under the **MIT License**.

## 📧 Contact
For support, contact **your.email@example.com** or open an issue on GitHub.

---

🚀 Happy Coding! 🎯


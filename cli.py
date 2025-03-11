import argparse
import csv
import logging
from pubmed_papers.fetcher import fetch_papers


def save_to_csv(papers, filename):
    """Saves fetched papers to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=papers[0].keys())
        writer.writeheader()
        writer.writerows(papers)


def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Save results to a CSV file")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    papers = fetch_papers(args.query)
    if not papers:
        print("No papers found.")
        return

    if args.file:
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)


if __name__ == "__main__":
    main()

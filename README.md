# Support Ticket Analyzer

A Python tool that analyzes support ticket data from a CSV file and generates a summary report.

## What It Does
- Reads ticket data from a CSV file
- Counts tickets by category and status
- Calculates average resolution time for closed tickets
- Handles missing files and malformed data gracefully

## Tech Stack
- Python 3
- `csv` module (built-in)
- `datetime` for date calculations
- `collections.defaultdict` for counting

## How to Run
1. Clone the repo
2. Ensure `tickets.csv` is in the same folder
3. Run: `python ticket_analyzer.py`

## Sample Output

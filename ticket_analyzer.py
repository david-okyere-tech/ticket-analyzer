import csv
from datetime import datetime
from collections import defaultdict

CSV_FILE = "tickets.csv"

def load_tickets(filename):
    """Read the CSV and return a list of ticket dictionaries."""
    tickets = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tickets.append(row)
        return tickets
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Make sure the file is in the same folder.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def analyze_tickets(tickets):
    """Calculate stats from the ticket data."""
    if not tickets:
        return

    total = len(tickets)
    category_counts = defaultdict(int)
    status_counts = defaultdict(int)
    resolution_days = []

    for ticket in tickets:
        # Count by category
        category = ticket.get("category", "Unknown")
        category_counts[category] += 1

        # Count by status
        status = ticket.get("status", "Unknown")
        status_counts[status] += 1

        # Calculate resolution time if resolved
        if status == "Resolved":
            created = ticket.get("created_date", "")
            resolved = ticket.get("resolved_date", "")
            if created and resolved:
                try:
                    start = datetime.strptime(created, "%Y-%m-%d")
                    end = datetime.strptime(resolved, "%Y-%m-%d")
                    days = (end - start).days
                    resolution_days.append(days)
                except ValueError:
                    pass

    # Print report
    print("=" * 40)
    print("SUPPORT TICKET ANALYSIS REPORT")
    print("=" * 40)
    print(f"Total Tickets: {total}\n")

    print("Tickets by Category:")
    for cat, count in sorted(category_counts.items()):
        print(f"  - {cat}: {count}")

    print("\nTickets by Status:")
    for stat, count in sorted(status_counts.items()):
        print(f"  - {stat}: {count}")

    if resolution_days:
        avg = sum(resolution_days) / len(resolution_days)
        print(f"\nAverage Resolution Time: {avg:.1f} days")
    else:
        print("\nAverage Resolution Time: N/A")

    print("=" * 40)

if __name__ == "__main__":
    tickets = load_tickets(CSV_FILE)
    analyze_tickets(tickets)
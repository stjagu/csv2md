# csv2md/cli.py
import csv
import sys

def convert(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if any(cell.strip() for cell in row)]

    if not rows:
        print("Empty or invalid CSV.")
        return

    header = '| ' + ' | '.join(rows[0]) + ' |'
    separator = '| ' + ' | '.join(['-' * max(len(cell), 3) for cell in rows[0]]) + ' |'
    body = ['| ' + ' | '.join(row) + ' |' for row in rows[1:]]

    print('\n'.join([header, separator] + body))

def main():
    if len(sys.argv) < 2:
        print("Usage: csv2md <file.csv>")
    else:
        convert(sys.argv[1])

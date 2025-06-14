# log_analyzer.py
import re
from collections import Counter


def analyze_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    error_lines = [line for line in logs if 'ERROR' in line]
    warning_lines = [line for line in logs if 'WARNING' in line]

    error_count = Counter([re.search(r'ERROR\s+(.*)', line).group(1) for line in error_lines if re.search(r'ERROR\s+(.*)', line)])
    warning_count = Counter([re.search(r'WARNING\s+(.*)', line).group(1) for line in warning_lines if re.search(r'WARNING\s+(.*)', line)])

    print("--- Log Summary ---")
    print(f"Total lines: {len(logs)}")
    print(f"Total errors: {len(error_lines)}")
    print(f"Total warnings: {len(warning_lines)}\n")

    print("Top Errors:")
    for error, count in error_count.most_common(5):
        print(f"{error}: {count}")

    print("\nTop Warnings:")
    for warning, count in warning_count.most_common(5):
        print(f"{warning}: {count}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Analyze a log file for errors and warnings.')
    parser.add_argument('file_path', help='Path to the log file')
    args = parser.parse_args()
    analyze_log(args.file_path)

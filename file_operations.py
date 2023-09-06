# file_operations.py
import os

def save_report_to_file(report_json, filename="security_assessment_report.json"):
    with open(filename, "w") as report_file:
        report_file.write(report_json)

def read_recipient_email(filename="recipient_email.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read().strip()
    else:
        return None

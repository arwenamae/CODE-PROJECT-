# reports.py
from file_handler import append_file, read_file

def create_report(username, items, location):
    reports = read_file("data/reports.txt")
    report_id = f"RPT-{len(reports)+1:03d}"
    line = f"{report_id}|{username}|{items}|{location}|Pending|0"
    append_file("data/reports.txt", line)
    print("Report submitted successfully.\n")

def get_user_reports(username):
    reports = read_file("data/reports.txt")
    return [r for r in reports if r.split("|")[1] == username]

def get_all_reports():
    return read_file("data/reports.txt")
# admin_dashboard.py
from reports import get_all_reports
from rewards import add_points
from file_handler import write_file, read_file
from auth import change_admin_password

def admin_menu():
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. View All Reports")
        print("2. Confirm Report and Award Points")
        print("3. View Redemption Requests")
        print("4. Change Admin Password")
        print("5. Logout")
        choice = input("Choose: ")

        if choice == '1':
            for r in get_all_reports():
                print(r.strip())

        elif choice == '2':
            rid = input("Enter Report ID to confirm: ")
            lines = read_file("data/reports.txt")
            new_lines = []
            for line in lines:
                parts = line.strip().split("|")
                if parts[0] == rid:
                    parts[4] = "Completed"
                    parts[5] = "10"  # fixed 10 pts per report
                    add_points(parts[1], 10)
                new_lines.append("|".join(parts) + "\n")
            write_file("data/reports.txt", new_lines)
            print("Report confirmed and points awarded.\n")

        elif choice == '3':
            redemptions = read_file("data/redemptions.txt")
            for r in redemptions:
                print(r.strip())

        elif choice == '4':
            change_admin_password()

        elif choice == '5':
            break
        else:
            print("Invalid choice.")
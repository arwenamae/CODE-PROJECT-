# user_dashboard.py
from reports import create_report, get_user_reports
from rewards import get_user_points, redeem_reward, get_available_rewards
from auth import change_user_password

def user_menu(username):
    while True:
        print("\n--- User Dashboard ---")
        print("1. Submit E-Waste Report")
        print("2. View My Reports")
        print("3. Redeem Rewards")
        print("4. Change Password")
        print("5. Logout")
        choice = input("Choose: ")

        if choice == '1':
            items = input("Enter items to report: ")
            location = input("Enter pickup location: ")
            create_report(username, items, location)

        elif choice == '2':
            reports = get_user_reports(username)
            print("\nYour Reports:")
            for r in reports:
                print(r.strip())

        elif choice == '3':
            points = get_user_points(username)
            print(f"\nPoints: {points}")
            rewards = get_available_rewards()
            for name, cost in rewards:
                print(f"- {name} ({cost} pts)")
            selected = input("Enter reward name to redeem: ")
            redeem_reward(username, selected)

        elif choice == '4':
            change_user_password(username)

        elif choice == '5':
            break
        else:
            print("Invalid choice.")
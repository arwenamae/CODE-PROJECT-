# main.py
from auth import login_admin, login_user
from admin_dashboard import admin_menu
from user_dashboard import user_menu

def main():
    print("\n=== E-WASTE MONITORING AND COLLECTION SYSTEM ===")
    print("1. Login as Admin")
    print("2. Login as User")
    choice = input("Enter your choice: ")

    if choice == '1':
        if login_admin():
            admin_menu()
    elif choice == '2':
        username = login_user()
        if username:
            user_menu(username)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

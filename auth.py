# auth.py
def login_admin():
    password = input("Enter admin password: ")
    with open("data/admin.txt", "r") as f:
        admin_pass = f.read().strip()
    if password == admin_pass:
        print("Admin login successful.\n")
        return True
    else:
        print("Incorrect admin password.")
        return False

def change_admin_password():
    old_pass = input("Enter current admin password: ")
    with open("data/admin.txt", "r") as f:
        current_pass = f.read().strip()
    if old_pass == current_pass:
        new_pass = input("Enter new password: ")
        with open("data/admin.txt", "w") as f:
            f.write(new_pass)
        print("Admin password updated.\n")
    else:
        print("Incorrect current password.")

def login_user():
    username = input("Username: ")
    password = input("Password: ")
    try:
        with open("data/users.txt", "r") as f:
            for line in f:
                user, pw, _ = line.strip().split("|")
                if user == username and pw == password:
                    print("User login successful.\n")
                    return username
        print("Invalid username or password.")
        return None
    except FileNotFoundError:
        print("User database not found.")
        return None

def change_user_password(username):
    old_pass = input("Enter current password: ")
    with open("data/users.txt", "r") as f:
        lines = f.readlines()
    new_lines = []
    updated = False
    for line in lines:
        user, pw, pts = line.strip().split("|")
        if user == username:
            if pw == old_pass:
                new_pass = input("Enter new password: ")
                new_lines.append(f"{user}|{new_pass}|{pts}\n")
                updated = True
            else:
                print("Incorrect current password.")
                return
        else:
            new_lines.append(line)
    if updated:
        with open("data/users.txt", "w") as f:
            f.writelines(new_lines)
        print("Password updated successfully.\n")
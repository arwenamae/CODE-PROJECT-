# rewards.py
from file_handler import read_file, write_file, append_file

def get_user_points(username):
    lines = read_file("data/users.txt")
    for line in lines:
        user, pw, pts = line.strip().split("|")
        if user == username:
            return int(pts)
    return 0

def add_points(username, points):
    lines = read_file("data/users.txt")
    new_lines = []
    for line in lines:
        user, pw, pts = line.strip().split("|")
        if user == username:
            pts = str(int(pts) + points)
        new_lines.append(f"{user}|{pw}|{pts}\n")
    write_file("data/users.txt", new_lines)

def redeem_reward(username, reward):
    rewards = dict([line.strip().split("|") for line in read_file("data/rewards.txt")])
    cost = int(rewards.get(reward, 0))
    user_points = get_user_points(username)
    if user_points >= cost:
        add_points(username, -cost)
        append_file("data/redemptions.txt", f"{username}|{reward}|Pending")
        print("Reward redeemed. Pending approval.\n")
    else:
        print("Not enough points.\n")


def get_available_rewards():
    return [line.strip().split("|") for line in read_file("data/rewards.txt")]
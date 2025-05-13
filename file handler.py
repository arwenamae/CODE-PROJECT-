# file_handler.py
def read_file(path):
    try:
        with open(path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def write_file(path, lines):
    with open(path, "w") as f:
        f.writelines(lines)

def append_file(path, line):
    with open(path, "a") as f:
        f.write(line + "\n")
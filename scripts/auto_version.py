import os
import time
from datetime import datetime

print("nohup python3 auto_version.py &")


def run_command(cmd):
    result = os.system(cmd)
    if result != 0:
        print(f"Command failed: {cmd}")
    return result


def has_changes():
    result = os.popen("git status --porcelain").read()
    return len(result.strip()) > 0


while True:
    try:
        if has_changes():
            run_command("git add .")
            commit_message = (
                f"Auto-commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            run_command(f'git commit -m "{commit_message}"')
        else:
            print(
                f"No changes detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(600)

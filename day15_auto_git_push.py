import subprocess
import datetime

def run_command(command):
    """Runs a shell command and prints output."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def auto_commit_push():
    # Step 1: Stage all changes
    run_command("git add .")

    # Step 2: Create a meaningful commit message with timestamp
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto commit on {date}"
    run_command(f'git commit -m "{commit_message}"')

    # Step 3: Push to GitHub
    run_command("git push origin main")

    print("\n✅ Auto commit and push completed successfully!")

if __name__ == "__main__":
    auto_commit_push()

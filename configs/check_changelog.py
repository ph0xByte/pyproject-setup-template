import subprocess
import sys


def has_changelog_changes():
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only'],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = result.stdout.splitlines()
        return 'CHANGELOG.md' in changed_files
    except subprocess.CalledProcessError as e:
        print(f"Error checking changelog changes: {e}")
        return False

if __name__ == "__main__":
    if not has_changelog_changes():
        print("ERROR: CHANGELOG.md must be updated before committing.")
        sys.exit(1)
    print("CHANGELOG.md has been updated.")

import sys
import subprocess


def is_poetry_installed() -> bool:
    try:
        subprocess.run(["poetry", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not is_poetry_installed():
        print("ERROR: Poetry is not installed. You need to install poetry https://python-poetry.org/docs/#installation")
        sys.exit(1)

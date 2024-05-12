import sys
import subprocess


def is_python_3_12_installed() -> bool:
    try:
        subprocess.run(
            ["python3.12", "--version"], capture_output=True, check=True
        )
        return True
    except Exception:
        return False


def is_poetry_installed() -> bool:
    try:
        subprocess.run(
            ["poetry", "--version"], capture_output=True, check=True
        )
        return True
    except Exception:
        return False


if __name__ == "__main__":
    if not is_python_3_12_installed():
        print(
            "ERROR: Python 3.12 is not installed. You need to install "
            "python 3.12 version https://www.python.org/downloads/"
        )
        sys.exit(1)

    if not is_poetry_installed():
        print(
            "ERROR: Poetry is not installed. You need to install "
            "poetry https://python-poetry.org/docs/#installation"
        )
        sys.exit(1)

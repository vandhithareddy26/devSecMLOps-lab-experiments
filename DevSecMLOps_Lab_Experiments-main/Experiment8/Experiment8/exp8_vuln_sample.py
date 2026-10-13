# ================================================================
# Experiment 8: ML utility with DELIBERATE vulnerabilities
# ================================================================

import pickle
import subprocess
import hashlib


def load_model(path):

    # VULNERABLE B301:
    # pickle.load on untrusted data can execute arbitrary code
    with open(path, "rb") as f:
        return pickle.load(f)


def run_cmd(user_input):

    # VULNERABLE B602:
    # shell=True with user input can cause command injection
    return subprocess.call(
        user_input,
        shell=True
    )


def checksum(data):

    # VULNERABLE B324:
    # MD5 is cryptographically broken
    return hashlib.md5(
        data.encode()
    ).hexdigest()


# VULNERABLE B105:
# Hard-coded password
DB_PASSWORD = "admin123"


def main():

    print("Experiment 8 - Vulnerability Scanning")

    print(
        "Vulnerable ML utility created."
    )

    print(
        "Run Bandit to identify security issues."
    )


if __name__ == "__main__":
    main()

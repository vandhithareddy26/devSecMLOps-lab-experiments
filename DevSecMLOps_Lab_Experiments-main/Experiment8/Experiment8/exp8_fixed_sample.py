# ================================================================
# Experiment 8: The SAME utility after remediation
# ================================================================

import json
import subprocess
import hashlib
import os


# ================================================================
# FIX 1: Replace unsafe pickle deserialization
# ================================================================

def load_model(path):

    # FIXED:
    # Load trusted model/configuration data using JSON
    # instead of unsafe pickle deserialization.

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


# ================================================================
# FIX 2: Remove shell=True
# ================================================================

def run_cmd(args_list):

    # FIXED:
    # Pass commands as a list and explicitly disable the shell.

    return subprocess.call(
        args_list,
        shell=False
    )


# ================================================================
# FIX 3: Replace MD5 with SHA-256
# ================================================================

def checksum(data):

    # FIXED:
    # SHA-256 is used instead of the weak MD5 algorithm.

    return hashlib.sha256(
        data.encode()
    ).hexdigest()


# ================================================================
# FIX 4: Remove hard-coded password
# ================================================================

# FIXED:
# Read the password from an environment variable.

DB_PASSWORD = os.environ.get(
    "DB_PASSWORD"
)


# ================================================================
# MAIN FUNCTION
# ================================================================

def main():

    print("================================================")
    print("Experiment 8 - Fixed ML Utility")
    print("================================================")

    print(
        "[FIXED] Unsafe pickle deserialization removed."
    )

    print(
        "[FIXED] shell=True removed."
    )

    print(
        "[FIXED] MD5 replaced with SHA-256."
    )

    print(
        "[FIXED] Hard-coded password removed."
    )

    print()
    print(
        "All security vulnerabilities have been remediated."
    )


# ================================================================
# PROGRAM ENTRY POINT
# ================================================================

if __name__ == "__main__":
    main()

import os
import re

# Constants
SOURCE_PATH = os.environ.get("SourcePath")
BUILD_NUM = os.environ.get("BuildNum")

# Validate environment variables
if not SOURCE_PATH or not BUILD_NUM:
    raise ValueError("Environment variables 'SourcePath' and 'BuildNum' must be set.")

SRC_DIR = os.path.join(SOURCE_PATH, "develop", "global", "src")
FILES_TO_UPDATE = {
    "SConstruct": r"(point)\s*=\s*\d+",  # Regex pattern for SConstruct file
    "VERSION": r"(ADLMSDK_VERSION_POINT)\s*=\s*\d+"  # Regex pattern for VERSION file
}


def update_file(filename, pattern):
    """Updates the version number in the specified file."""
    file_path = os.path.join(SRC_DIR, filename)
    temp_file_path = file_path + ".tmp"

    try:
        with open(file_path, "r") as fin, open(temp_file_path, "w") as fout:
            for line in fin:
                fout.write(re.sub(pattern, rf"\1={BUILD_NUM}", line))

        # Replace the original file with the modified file
        os.replace(temp_file_path, file_path)
        print(f"Updated {filename} successfully.")

    except FileNotFoundError:
        print(f"Error: {filename} not found in {SRC_DIR}.")
    except PermissionError:
        print(f"Error: No permission to modify {filename}.")
    except Exception as e:
        print(f"Unexpected error while updating {filename}: {e}")


def main():
    """Main function to update version numbers in files."""
    for file, pattern in FILES_TO_UPDATE.items():
        update_file(file, pattern)


if __name__ == "__main__":
    main()


# -------------
# Issues with the Original Code
# -------------
# 1. Hardcoded Paths - Paths are manually concatenated multiple times → error-prone.
# 2. Repeated Code - The logic for reading, modifying, and writing files is duplicated.
# 3. No Exception Handling - If files are missing or permissions are incorrect, the script will fail.
# 4. Old Python Syntax - 0755 is invalid in Python 3.
# 5. No Logging or User Feedback
# 6. regex pattern does not account for spaces around the = sign

import os

# LAB 7 - DIRECTORY SCANNING WITH EXCEPTION HANDLING


# User-defined Exception
class MissingFileOrFolderError(Exception):

    """Raised when a required file or folder is missing."""

    pass


# Function to Scan Directory
def scan_directory(path):

    try:

        # Step 1: Check if Path Exists
        if not os.path.exists(path):

            raise FileNotFoundError(
                f"Invalid directory path: {path}"
            )

        print(f"\nScanning directory: {path}\n")

        # Step 2: Walk Through Directory Structure
        for root, dirs, files in os.walk(path):

            level = root.replace(path, "").count(os.sep)

            indent = " " * 4 * level

            print(f"{indent}{os.path.basename(root)}/")

            sub_indent = " " * 4 * (level + 1)

            # Display Files
            for f in files:

                print(f"{sub_indent}{f}")

            # Step 3: Raise Custom Exception for Empty Folder
            if not files and not dirs:

                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

    except FileNotFoundError as e:

        print(f"Error: {e}")

    except MissingFileOrFolderError as e:

        print(f"Custom Error: {e}")

    except Exception as e:

        print(f"Unexpected Error: {e}")


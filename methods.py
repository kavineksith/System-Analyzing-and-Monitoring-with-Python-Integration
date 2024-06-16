import json
import os
import sys
from pathlib import Path


def create_directory_and_generate_file_path(base_directory, file_name):
    """
    Creates a directory if it doesn't already exist and generates a file path.

    Args:
    - base_directory (str): Base directory path where the directory will be created and the file path will be generated.
    - file_name (str): Name of the file (including extension).

    Returns:
    - str: Full file path.
    """
    # Create directory if it doesn't exist
    directory_path = Path(base_directory)
    directory_path.mkdir(parents=True, exist_ok=True)

    # Generate file path
    file_path = directory_path / file_name

    return str(file_path)


def control_result_to_json(statistics):
    try:
        # User input for base directory and file name
        base_directory = input("Enter base directory path: ").strip()
        file_name = input("Enter file name (including extension): ").strip()

        # Generate file path and create directory if necessary
        file_path = create_directory_and_generate_file_path(base_directory, file_name)
        print(f"Generated file path: {file_path}")

        # Write the dictionary to JSON file
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(statistics, json_file, indent=4, ensure_ascii=False)

        print("JSON data has been saved to", file_path)
    except ValueError as ve:
        print(ve)
        sys.exit(1)
    # except FileNotFoundError:
    #     print("Source file not found.")
    #     sys.exit(1)
    except PermissionError:
        print("Permission denied to access the source or export file.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print("Error uploading data:", e)
        sys.exit(1)

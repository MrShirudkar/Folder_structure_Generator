import os

def generate_folder_structure(folder_path, indent=0):
    if not os.path.exists(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return

    if os.path.isfile(folder_path):
        print("Error: The specified path is a file, not a folder.")
        return

    folder_name = os.path.basename(folder_path)
    print(f"{' ' * indent}├── {folder_name}")

    try:
        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    generate_folder_structure(entry.path, indent + 3)
                elif entry.is_file():
                    file_name = os.path.basename(entry.path)
                    print(f"{' ' * (indent + 3)}├── {file_name}")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the folder path for which you want to generate the structure
    folder_to_check = "Your Folder Path"

    generate_folder_structure(folder_to_check)

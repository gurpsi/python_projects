import os

def search_files(directory, search_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    if search_text in content:
                        print(f"Found '{search_text}' in: {file_path}")
            except UnicodeDecodeError:
                print(f"Error reading file: {file_path} (UnicodeDecodeError)")

# Provide the directory path to search in and the text to search for
directory_path = 'path/to/directory'
search_text = 'specific text'

search_files(directory_path, search_text)
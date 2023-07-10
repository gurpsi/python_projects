import os

def search_files(directory, search_text, output_file):
    with open(output_file, 'w') as out:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if search_text in content:
                            out.write(f"Found '{search_text}' in: {file_path}\n")
                except UnicodeDecodeError:
                    out.write(f"Error reading file: {file_path} (UnicodeDecodeError)\n")

# Provide the directory path to search in, the text to search for, and the output file path
directory_path = 'path/to/directory'
search_text = 'specific text'
output_file_path = 'path/to/output/file.txt'

search_files(directory_path, search_text, output_file_path)

import os

def search_files(directory, file_extension, search_text, output_file):
    with open(output_file, 'w') as out:
        for file in os.listdir(directory):
            if file.endswith(file_extension):
                file_path = os.path.join(directory, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if search_text in content:
                            out.write(f"Found '{search_text}' in: {file_path}\n")
                except UnicodeDecodeError:
                    out.write(f"Error reading file: {file_path} (UnicodeDecodeError)\n")

# Provide the directory path to search in, the file extension to filter, the text to search for, and the output file path
directory_path = 'path/to/directory'
file_extension = '.txt'  # Specify the desired file extension (e.g., '.txt', '.csv')
search_text = 'specific text'
output_file_path = 'path/to/output/file.txt'

search_files(directory_path, file_extension, search_text, output_file_path)

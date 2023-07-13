import os

def search_file(filename, search_path):
    found_files = []

    for root, dirs, files in os.walk(search_path):
        if 'Archive' in dirs:
            dirs.remove('Archive')  # Exclude the 'Archive' folder from the search

        if filename in files:
            file_path = os.path.join(root, filename)
            found_files.append(file_path)

    return found_files

# Example usage
search_path = '/path/to/search'  # Replace with the path where you want to start searching
filename = 'target_file.txt'  # Replace with the specific file you're looking for

found_files = search_file(filename, search_path)
if found_files:
    print("Found files:")
    for file_path in found_files:
        print(file_path)
else:
    print("No files found.")
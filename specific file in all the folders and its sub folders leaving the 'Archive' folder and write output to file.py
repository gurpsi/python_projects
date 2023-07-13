import os

def search_file(filename, search_path, output_file):
    found_files = []

    for root, dirs, files in os.walk(search_path):
        if 'Archive' in dirs:
            dirs.remove('Archive')  # Exclude the 'Archive' folder from the search

        if filename in files:
            file_path = os.path.join(root, filename)
            found_files.append(file_path)

    if found_files:
        with open(output_file, 'w') as f:
            f.write("Found files:\n")
            for file_path in found_files:
                f.write(file_path + '\n')
        print("Results written to", output_file)
    else:
        print("No files found.")

# Example usage
search_path = '/path/to/search'  # Replace with the path where you want to start searching
filename = 'target_file.txt'  # Replace with the specific file you're looking for
output_file = '/path/to/output.txt'  # Replace with the path of the output file

search_file(filename, search_path, output_file)

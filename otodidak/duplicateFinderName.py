import os
import shutil

# Define the paths for the folders
raw_folder = r"C:\Users\amriz\Downloads\torrent\done"
best_folder = r"C:\Users\amriz\Downloads\torrent\done\jep"
duplicated_folder = r"C:\Users\amriz\Downloads\torrent\duplicated"

# Create the "duplicated" folder if it doesn't exist
if not os.path.exists(duplicated_folder):
    os.makedirs(duplicated_folder)

# Get the list of files in the "raw" and "best" folders
raw_files = set(os.listdir(raw_folder))
best_files = set(os.listdir(best_folder))

# Find the intersection of filenames (duplicates)
duplicated_files = raw_files.intersection(best_files)

# Move the duplicated files from "raw" to "duplicated"
moved_files = []
for file_name in duplicated_files:
    src_path = os.path.join(raw_folder, file_name)
    dest_path = os.path.join(duplicated_folder, file_name)
    shutil.move(src_path, dest_path)
    moved_files.append(file_name)

# Print the names of the moved files and the total count
if moved_files:
    print("\nFiles moved:")
    for file in moved_files:
        print(file)
    print(f"\n{len(moved_files)} files have been moved.")
else:
    print("No files were moved.")
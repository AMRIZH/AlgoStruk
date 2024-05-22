import os
import shutil

# Define the paths for the folders
raw_folder = r"C:\Users\amriz\Downloads\torrent\done"
best_folder = r"C:\Users\amriz\Downloads\torrent\done\kuroinu"
duplicated_folder = r"C:\Users\amriz\Downloads\torrent\duplicated"

# Create the "duplicated" folder if it doesn't exist
if not os.path.exists(duplicated_folder):
    os.makedirs(duplicated_folder)

# Get the list of files/folders and their sizes in the "raw" and "best" folders
raw_items = {item: os.path.getsize(os.path.join(raw_folder, item)) for item in os.listdir(raw_folder)}
best_items = {item: os.path.getsize(os.path.join(best_folder, item)) for item in os.listdir(best_folder)}

# Find the duplicates based on name and size
duplicated_items = []
for item_name, item_size in raw_items.items():
    if item_name in best_items and best_items[item_name] == item_size:
        duplicated_items.append(item_name)

# Move the duplicated items from "raw" to "duplicated"
moved_items = []
for item_name in duplicated_items:
    src_path = os.path.join(raw_folder, item_name)
    dest_path = os.path.join(duplicated_folder, item_name)
    shutil.move(src_path, dest_path)
    moved_items.append(item_name)

# Print the names of the moved items and the total count
if moved_items:
    print("\nItems moved:")
    for item in moved_items:
        print(item)
    print(f"\n{len(moved_items)} items have been moved.")
else:
    print("No items were moved.")
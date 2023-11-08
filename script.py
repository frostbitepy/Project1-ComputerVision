import os

def get_folders_names(directory):
    # Get all folders recursively from the specified directory
    folders = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if os.path.isdir(os.path.join(root, filename)):
                folders.append(filename)
    
    return folders

# Specify the directory path
directory = "train"

# Get all folder names
folders_names = get_folders_names(directory)

# Print the list of folder names
print(folders_names)
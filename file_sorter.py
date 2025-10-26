"""
File sorter module.
Contains functions for organizing files by type.
"""
import os
import shutil

# Define file categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".json", ".xml", ".sql"],
    "Executables": [".exe", ".dmg", ".app", ".deb", ".rpm"],
}

def get_file_category(filename):
    """Determine the category of a file based on its extension."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    
    return "Others"

def sort_files(directory):
    """Sort files in the given directory into categorized subdirectories."""
    # Get list of files in directory
    try:
        items = os.listdir(directory)
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'")
        return
    
    files_moved = 0
    
    for item in items:
        item_path = os.path.join(directory, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue
        
        # Determine category
        category = get_file_category(item)
        
        # Create category folder if it doesn't exist
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created folder: {category}")
        
        # Move file to category folder
        destination = os.path.join(category_path, item)
        
        # Handle duplicate filenames
        if os.path.exists(destination):
            base, ext = os.path.splitext(item)
            counter = 1
            while os.path.exists(destination):
                new_name = f"{base}_{counter}{ext}"
                destination = os.path.join(category_path, new_name)
                counter += 1
        
        try:
            shutil.move(item_path, destination)
            print(f"Moved: {item} → {category}/")
            files_moved += 1
        except Exception as e:
            print(f"Error moving {item}: {e}")
    
    print(f"\nTotal files organized: {files_moved}")


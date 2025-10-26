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
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".json", ".xml", ".sql", ".verse"],
    "Executables": [".exe", ".dmg", ".app", ".deb", ".rpm"],
}

def get_file_category(filename):
    file_extension = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Others"

def analyze_files(directory):
    categorized_files = {}
    files = os.listdir(directory)
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            category = get_file_category(file)
            if category not in categorized_files:
                categorized_files[category] = []
            categorized_files[category].append(file)

    return categorized_files

def sort_files(directory, file_dictionary):
    for category, files in file_dictionary.items():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        for file in files:
            source_file_path = os.path.join(directory, file)
            shutil.move(source_file_path, folder_path)
    


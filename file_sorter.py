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
    "Photoshop": [".psd", ".psb", ".xcf"],
    "Illustrator": [".ai", ".eps", ".svg"],
    "InDesign": [".indd", ".idml", ".indt"],
    "Acrobat": [".pdf", ".acrobat", ".acrobatpro", ".acrobatreader", ".acrobatreaderdc", ".acrobatreaderdcx", ".acrobatreaderdcx2", ".acrobatreaderdcx3", ".acrobatreaderdcx4", ".acrobatreaderdcx5", ".acrobatreaderdcx6", ".acrobatreaderdcx7", ".acrobatreaderdcx8", ".acrobatreaderdcx9", ".acrobatreaderdcx10"],
    "Excel": [".xls", ".xlsx", ".xlsm", ".xlsb", ".xls2003", ".xls2003xml", ".xls2003xml2", ".xls2003xml3", ".xls2003xml4", ".xls2003xml5", ".xls2003xml6", ".xls2003xml7", ".xls2003xml8", ".xls2003xml9", ".xls2003xml10"],
    "PowerPoint": [".ppt", ".pptx", ".pptm", ".pptx2003", ".pptx2003xml", ".pptx2003xml2", ".pptx2003xml3", ".pptx2003xml4", ".pptx2003xml5", ".pptx2003xml6", ".pptx2003xml7", ".pptx2003xml8", ".pptx2003xml9", ".pptx2003xml10"],
    "Word": [".doc", ".docx", ".docm", ".docx2003", ".docx2003xml", ".docx2003xml2", ".docx2003xml3", ".docx2003xml4", ".docx2003xml5", ".docx2003xml6", ".docx2003xml7", ".docx2003xml8", ".docx2003xml9", ".docx2003xml10"],
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
    


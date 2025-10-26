"""
Main entry point for the file sorter application.
"""
import file_sorter as fs
import os


def main():
    """Main application loop."""
    print("Welcome to the file sorter application by janxyz.")
    print("Enter the directory path you want to organize:")
    directory = input().strip()
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return
    files_per_category = fs.analyze_files(directory)
    print("\nFound files:")
    for category, files in files_per_category.items():
        print(f"  {category}: {len(files)} files")
    confirm = input("\nProceed with sorting? (y/n): ")
    if confirm.lower() == "y":
        fs.sort_files(directory, files_per_category)
        print("Successfuly sorted files.")


if __name__ == "__main__":
    main()


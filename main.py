"""
Main entry point for the file sorter application.
"""
import file_sorter
import os

def main():
    print("\n=== File Sorter by janxyz ===")
    print("This tool helps organize files in a directory by type.")
    print("-" * 40)
    
    while True:
        print("\n1. Sort files in a directory")
        print("2. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            directory = input("Enter the directory path to sort: ").strip()
            
            if not os.path.exists(directory):
                print(f"Error: Directory '{directory}' does not exist.")
                continue
            
            if not os.path.isdir(directory):
                print(f"Error: '{directory}' is not a directory.")
                continue
            
            print(f"\nScanning directory: {directory}")
            file_sorter.sort_files(directory)
            print("\n✓ Files sorted successfully!")
            
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


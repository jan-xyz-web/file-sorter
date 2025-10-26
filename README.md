# File Sorter

A Python application that automatically organizes files in a directory by categorizing them into folders based on their file types.

## Features

- Automatically sorts files into categories:
  - Images (jpg, png, gif, etc.)
  - Documents (pdf, docx, txt, etc.)
  - Videos (mp4, avi, mkv, etc.)
  - Audio (mp3, wav, flac, etc.)
  - Archives (zip, rar, 7z, etc.)
  - Code (py, js, html, etc.)
  - Executables (exe, dmg, app, etc.)
  - Others (uncategorized files)

- Handles duplicate filenames automatically
- Interactive command-line interface
- Safe file moving (no data loss)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jan-xyz-web/file_sorter.git
cd file_sorter
```

2. No external dependencies required - uses only Python standard library!

## Usage

Run the application:
```bash
python main.py
```

Follow the prompts to:
1. Enter the directory path you want to organize
2. Watch as files are automatically sorted into category folders

## Example

Before:
```
Downloads/
├── photo.jpg
├── document.pdf
├── song.mp3
└── video.mp4
```

After running File Sorter:
```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── document.pdf
├── Audio/
│   └── song.mp3
└── Videos/
    └── video.mp4
```

## Author

Created by janxyz

## License

MIT License


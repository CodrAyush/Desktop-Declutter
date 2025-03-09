# Desktop Declutter

Desktop Declutter is a Python script designed to organize files on your desktop by moving them into custom folders based on their file types and sorting them by modification date. The script also backs up files before moving them to ensure data safety.

## Features

- **Custom Folders**: Automatically creates and organizes files into user-defined folders based on file extensions
- **Backup**: Creates a backup of each file before moving it to ensure data safety
- **Sorting**: Additional sorting of files by modification date into dated folders
- **Configuration**: Easily customizable through a JSON configuration file
- **Command-Line Arguments**: Support for custom configuration file paths
- **Logging**: Detailed logging of all operations for tracking and debugging

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CodrAyush/File-Organizer.git
cd File-Organizer
```

2. No additional dependencies required! The script uses only Python standard library modules.

## Configuration

1. Open `config.json` and update the `desktop_path` to your desktop location:

```json
{
    "desktop_path": "C:\\Users\\YourUsername\\Desktop",
    "custom_folders": {
        "Photos": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".doc", ".docx", ".txt", ".pdf"],
        "Music": [".mp3", ".wav"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Code": [".py", ".cpp", ".java", ".sh"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Executables": [".exe", ".msi"],
        "Others": []
    },
    "ignore_files": ["file_organizer.log", "config.json"]
}
```

You can:
- Modify the file extensions for each folder
- Add new folders with custom extensions
- Update the ignore_files list to prevent certain files from being moved

## Usage

Run the script using:

```bash
python organize_files.py
```

Or specify a custom config file:

```bash
python organize_files.py --config path/to/config.json
```

## Output Structure

The script organizes your files into this structure:

```
Desktop/
├── Backup/                 # Backup of all moved files
├── Photos/                 # Image files
├── Documents/              # Document files
├── Music/                  # Audio files
├── Videos/                 # Video files
├── Code/                   # Source code files
├── Archives/               # Compressed files
├── Executables/            # Executable files
└── Sorted Files/          # Files sorted by date
    └── YYYY-MM-DD/        # Date-based folders
```

## Logging

All operations are logged in `file_organizer.log` with timestamps:

```
2024-01-01 12:00:00 - INFO - Backed up file example.txt to Backup folder
2024-01-01 12:00:01 - INFO - Moved file example.txt to Documents
```

## Safety Features

- All files are backed up before being moved
- Duplicate filenames are handled by appending timestamps
- Error logging for failed operations
- Configurable file ignore list

## Error Handling

The script includes comprehensive error handling:
- Logs all errors with timestamps
- Continues operation even if individual file operations fail
- Creates missing directories as needed

## Contributing

Feel free to:
- Report issues
- Submit pull requests
- Suggest new features
- Improve documentation

## License

This project is licensed under the terms included in the LICENSE file.

# py-merger

This Python script copies the contents of a source directory to a destination directory, creating new folders and files as needed. It also allows for selective copying by skipping folders and files based on regular expression patterns.

### Requirements

- Python 3.x

### Setup

1. Create a `.env` file in the same directory as the script with the following variables:

   ```
   # Paths to the source and destination directories
   SOURCE_DIR=/path/to/your/source/directory
   DESTINATION_DIR=/path/to/your/destination/directory

   # Optional: Regular expressions for folders and files to skip
   FOLDERS_TO_SKIP_REGEX=^temp\/$
   FILES_TO_SKIP_REGEX=\.tmp$
   ```

### Usage

1. Activate your virtual environment (if applicable).
2. Run the script from the command line:

   ```bash
   py main.py
   ```

### Additional Information

- The script uses the `shutil` module for file and directory operations.
- It utilizes regular expressions to match folders and files for skipping.
- It creates new folders and files in the destination directory if they don't exist.

### Further Customization

- Modify the script code directly for fine-grained control over the copying process.
- Add more environment variables or command-line arguments to enhance its flexibility.

### Troubleshooting

- Ensure correct path names in the `.env` file.
- Double-check regular expression patterns for accuracy.
- Check for write permissions in the destination directory.
- If you encounter issues, refer to the Python documentation for `shutil` and regular expressions.

# File Organizer

File Organizer is a Python script designed to automate the organization of files within specified directories based on their types. This utility intelligently categorizes files such as documents, images, videos, and more into designated folders, facilitating better organization and easy access to files.

## Features
- Automatically sorts files into folders based on their types.
- Customizable configurations to tailor the organization process according to specific needs.
- Simplifies file management by keeping directories neat and clutter-free.
- Seamless integration with existing file systems.
- Easy-to-use interface for effortless organization of digital files.

## Usage
To run the File Organizer script:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Modify the configuration in the script as needed (optional).
4. Run the script using Python:

```bash
python main.py
```

## Building Executable
To convert the Python script into an executable (.exe) file:

1. Ensure that you have installed PyInstaller.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

```bash
pip install pyinstaller

pyinstaller --onefile --windowed main.py
```

5. The executable file will be generated in the `dist` directory.

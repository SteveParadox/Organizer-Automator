import os
import shutil
import time

# A dictionary with file types and their corresponding directories
file_types = {
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "pdf": "PDFs",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Text",
    "xlsx": "Spreadsheets",
    "csv": "Spreadsheets",
    "mp3": "Music",
    "mp4": "Videos",
    "avi": "Videos",
    "exe": "Executables",
    "pptx": "Power Point",
    "mkv": "Videos",
    "ps1": " Windows Power Shell",
    "apk": "Android Applications",
    "psd": "Photo Shops",
    "html": "Html codes",
    "py": "Python codes",
    "js": "JavaScript codes",
    "json": "Json files"
}

# function to move files to their corresponding directories
def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory not found.. Damnnn")
        return

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_type = filename.split(".")[-1].lower()
            if file_type in file_types:
                directory_name = file_types[file_type]
                destination_directory = os.path.join(directory, directory_name)
                if not os.path.exists(destination_directory):
                    os.makedirs(destination_directory) # Using makedirs instead of mkdir to create nested directories
                source_path = os.path.join(directory, filename)
                destination_path = os.path.join(destination_directory, filename)
                shutil.move(source_path, destination_path)
                time.sleep(0.2)

        

# Calliing the function to organize files in the specified directory
organize_files("C:/Users/USER/Desktop")

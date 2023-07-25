import os
import zipfile
import re
import sys
from bs4 import BeautifulSoup

def replace_string_in_file(file_path):
    with open(file_path, 'r') as file:
        filedata = file.read()
        
    # Replace the target string
    filedata = filedata.replace('<script type=application/vnd.jupyter.widget-state+json>', '<script type="application/vnd.jupyter.widget-state+json">')

    # Write the file out again
    with open(file_path, 'w') as file:
        file.write(filedata)


def replace_in_epub(epub_path):
    # Create temporary directory for epub content
    os.system(f'mkdir tmp')

    # Unzip the epub
    os.system(f'unzip {epub_path} -d tmp')

    # Walk through the directory
    for root, dirs, files in os.walk("tmp"):
        for file in files:
            if file.endswith(".xhtml"):
                file_path = os.path.join(root, file)
                replace_string_in_file(file_path)

    # Removing the original epub file
    os.system(f'rm {epub_path}')

    # Zipping files back into an epub
    os.system(f'cd tmp && zip -Xr9D ../{epub_path} mimetype *')

    # Remove temporary directory
    os.system('rm -r tmp')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <epub_path>")
        sys.exit(1)

    epub_path = sys.argv[1]
    replace_in_epub(epub_path)


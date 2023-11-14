"""
This script takes a single directory as a command line argument and iterates through
all its subdirectories. For each subdirectory, it checks for the presence of '.mkv' files.
If no '.mkv' files are found, it searches for '.rar' files and extracts them if found.

Usage:
  python script.py [parent_directory]

Example:
  python script.py /path/to/parent/directory
"""

import os
import subprocess
import sys

def extract_rar(file_path):
  directory = os.path.dirname(file_path)
  command = f"unrar x -o+ '{file_path}' '{directory}'"
  subprocess.run(command, shell=True)

def process_directory(directory):
  has_mkv = any(file.endswith('.mkv') for file in os.listdir(directory))
  if not has_mkv:
    for file in os.listdir(directory):
      if file.endswith('.rar'):
        rar_file = os.path.join(directory, file)
        print(f"Extracting {rar_file}")
        extract_rar(rar_file)

def main(parent_directory):
  for root, dirs, files in os.walk(parent_directory):
    process_directory(root)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py [parent_directory]")
  else:
    parent_directory = sys.argv[1]
    main(parent_directory)

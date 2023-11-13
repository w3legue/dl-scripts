# save this as download_complete.py

import sys
import os
import subprocess

def extract_rar(file_path):
  # command to extract rar files
  command = f"unrar x -o+ '{file_path}'"
  subprocess.run(command, shell=True)

def main(torrent_id, torrent_name, save_path):
  # Build the full path to the torrent's directory
  torrent_directory = os.path.join(save_path, torrent_name)

  # Check if the path exists and is a directory
  if os.path.exists(torrent_directory) and os.path.isdir(torrent_directory):
    # Iterate over files in the directory
    for file in os.listdir(torrent_directory):
      if file.endswith(".rar"):
        # Full path to the rar file
        rar_file = os.path.join(torrent_directory, file)
        print(f"Extracting {rar_file}")
        extract_rar(rar_file)
  else:
    print("Directory does not exist or is not a directory")

if __name__ == "__main__":
  if len(sys.argv) < 4:
    print("Usage: python download_complete.py [TorrentID] [TorrentName] [SavePath]")
  else:
    torrent_id = sys.argv[1]
    torrent_name = sys.argv[2]
    save_path = sys.argv[3]
    main(torrent_id, torrent_name, save_path)

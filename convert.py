#convert script
import os
from fontTools.ttLib import TTFont

def convert_ttf_to_woff(ttf_path, woff_path):
    font = TTFont(ttf_path)
    font.flavor = 'woff'
    font.save(woff_path)

def convert_all_ttf_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ttf"):
            ttf_path = os.path.join(directory, filename)
            woff_path = os.path.join(directory, filename.replace(".ttf", ".woff"))
            try:
                convert_ttf_to_woff(ttf_path, woff_path)
                print(f"Converted {ttf_path} to {woff_path}")
            except Exception as e:
                print(f"Failed to convert{ttf_path}: {e}")

# Example usage
# just change the path to the path you desire. 
directory = 'C:\\Users\\Public\Documents\\ttf'
convert_all_ttf_in_directory(directory)

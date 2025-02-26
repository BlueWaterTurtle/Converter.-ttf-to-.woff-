#convert script
#this one converts .ttf files to .woff, .woff2, and otf. 
import os
from fontTools.ttLib import TTFont

def convert_ttf_to_woff(ttf_path, woff_path):
    font = TTFont(ttf_path)
    font.flavor = 'woff'
    font.save(woff_path)

def convert_ttf_to_woff2(ttf_path, woff2_path):
    font = TTFont(ttf_path)
    font.flavor = 'woff2'
    font.save(woff2_path)

def convert_ttf_to_otf(ttf_path, otf_path):
    font = TTFont(ttf_path)
    font.flavor = None  # OTF has no special flavor
    font.save(otf_path)

def convert_all_ttf_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".ttf"):
            ttf_path = os.path.join(directory, filename)
            woff_path = os.path.join(directory, filename.replace(".ttf", ".woff"))
            woff2_path = os.path.join(directory, filename.replace(".ttf", ".woff2"))
            otf_path = os.path.join(directory, filename.replace(".ttf", ".otf"))
            try:
                convert_ttf_to_woff(ttf_path, woff_path)
                convert_ttf_to_woff2(ttf_path, woff2_path)
                convert_ttf_to_otf(ttf_path, otf_path)
                print(f"Converted {ttf_path} to {woff_path}, {woff2_path}, and {otf_path}")
            except Exception as e:
                print(f"Failed to convert {ttf_path}: {e}")

# Example usage
directory = r'C:\Users\Public\Documents\ttf'
convert_all_ttf_in_directory(directory)

# Keep the window open
input("Press Enter to exit...")

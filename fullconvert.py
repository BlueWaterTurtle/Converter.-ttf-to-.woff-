import os
import logging
from fontTools.ttLib import TTFont
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FontConverter:
    def __init__(self, directory):
        self.directory = directory

    def convert_ttf_to_woff(self, ttf_path, woff_path):
        font = TTFont(ttf_path)
        font.flavor = 'woff'
        font.save(woff_path)

    def convert_ttf_to_woff2(self, ttf_path, woff2_path):
        font = TTFont(ttf_path)
        font.flavor = 'woff2'
        font.save(woff2_path)

    def convert_ttf_to_otf(self, ttf_path, otf_path):
        font = TTFont(ttf_path)
        font.flavor = None  # OTF has no special flavor
        font.save(otf_path)

    def convert_file(self, filename):
        ttf_path = os.path.join(self.directory, filename)
        woff_path = os.path.join(self.directory, filename.replace(".ttf", ".woff"))
        woff2_path = os.path.join(self.directory, filename.replace(".ttf", ".woff2"))
        otf_path = os.path.join(self.directory, filename.replace(".ttf", ".otf"))
        try:
            self.convert_ttf_to_woff(ttf_path, woff_path)
            self.convert_ttf_to_woff2(ttf_path, woff2_path)
            self.convert_ttf_to_otf(ttf_path, otf_path)
            logging.info(f"Converted {ttf_path} to {woff_path}, {woff2_path}, and {otf_path}")
        except Exception as e:
            logging.error(f"Failed to convert {ttf_path}: {e}")

    def convert_all_ttf_in_directory(self):
        with ThreadPoolExecutor() as executor:
            for filename in os.listdir(self.directory):
                if filename.endswith(".ttf"):
                    executor.submit(self.convert_file, filename)

if __name__ == "__main__":
    directory = r'C:\Users\Public\Documents\ttf'
    converter = FontConverter(directory)
    converter.convert_all_ttf_in_directory()
    input("Press Enter to exit...")

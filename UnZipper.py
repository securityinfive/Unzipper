# The UnZipper. Simply, run it in the directory where you have 1 or many zip files and will extract them into a new folder called 'Unzipped'. 
# Written for mass unzipping of hundreds of zip files. 

# note - in your terminal, navigate to the root folder where your zip files are stored. This will use that rather than you needed to edit the
# code to the folder path. 

import zipfile
import os

def unzip_all_zips_in_folder(zip_folder, extract_root):
    # Create root extraction folder if it doesn't exist
    os.makedirs(extract_root, exist_ok=True)
                    
    for filename in os.listdir(zip_folder):
        if filename.lower().endswith('.zip'):
            zip_path = os.path.join(zip_folder, filename)
            extract_to = os.path.join(extract_root)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
                print(f'Extracted {filename} to {extract_to}')

# Start
current_dir = os.getcwd()
extract_dir = 'unzipped'            # Where to place unzipped folders

unzip_all_zips_in_folder(current_dir, extract_dir)
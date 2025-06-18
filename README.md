# Unzipper
Unzipper is a simple python script to unzip one or a large amount of zip files. This little script came about from downloading PDF files from vendors that were all zipped, downloading ROMS, ringtones, backups where they would zip them. Got sick and tire of manually going to each one or using a ZIP tool, so I wrote this.

**USE**

This script is intended to be ran from the 'root' directory where your ZIP files are stored. 

For example your ZIP files are stored in **C:\Downloads\ZIPs**

Open your Python editor of choice or a terminal windows and navigate to **C:\Downloads\ZIPs** then run the **Unzipper.py** file.

The script will detect the directory and create a new folder called **unzipped** (if it doesn't already exist). 

The script will iterate through the directory and unzip all the ZIP files it finds in the directory (**C:\Downloads\ZIPs**) and put all the contents in unzipped.

It will NOT create sub folders for each zip file, just all the contents in **C:\Downloads\ZIPs\unzipped**.

That's it. 

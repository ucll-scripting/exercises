
from zipfile import ZipFile
from datetime import datetime
import argparse
import os


def parser():
    parser = argparse.ArgumentParser(prog="backup")
    parser.add_argument("backupdirectory",help="Path to backupdirectory")
    parser.add_argument("important_files",help="list of files")
    return parser
args = parser().parse_args()
backupdirectory = args.backupdirectory
important_files = args.important_files

filepaths = []
for root, dirs, files in os.walk(important_files, topdown=False):
    for name in files:
        path = os.path.join(root, name)
        filepaths.append(path)
        
print('Following files will be zipped:')
for file_name in filepaths:
    print(file_name)


with ZipFile(backupdirectory+"\EAR-MONTH-DAY.zip",'w') as backup:
    # writing each file one by one
    for file in filepaths:
        backup.write(file)
  
    print('All files zipped successfully!')   

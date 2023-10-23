import os
import re

# parse file tree in Downloads folder
path = "C:/Users/User/Downloads"  # path to Downloads folder
files = os.listdir(path)  # gather list of files in folder
exts = set()  # set to store uq file exts

# access file ext in Downloads dir
for file in files:
    ext = re.findall(r'[.](\w+)$', file)
    
    # if no extension, skip
    if len(ext) == 0:
        continue
    
    # gather all extensions
    exts.add(ext[0].lower())

print(exts)
    

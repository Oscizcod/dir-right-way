import os
import re
import shutil as st

# parse file tree in Downloads folder
path = "C:/Users/User/Downloads/"  # path to Downloads folder
files = os.listdir(path)  # gather list of files in folder
exts = set()  # set to store uq file exts
# sort exts into lists
images = ['png', 'jpeg', 'jpg']
docs = ['doc', 'docx', 'txt', 'pdf', 'rmd', 'odt', 'epub']
data = ['csv', 'xlsx', 'json']
code = ['py', 'ipynb', 'html']
list_dirs = ['images', 'docs', 'data', 'code', 'misc']  # list of dirs to create

# create all dirs in Downloads dir
for dir in list_dirs:
    if os.path.exists(path + dir):
        print(f'{dir}/ dir exists')
    else:
        os.mkdir(path + dir)

# get file extensions
for file in files:
    if os.path.isdir(path + file):  # skip dirs
        continue 
    else:
        ext = re.findall(r'[.](\w+)$', file)
    
    # sort extension into dirs
    # if no extension, put in misc
    if len(ext) == 0:
        st.move(path + file, path + 'misc/' + file)
        continue
    elif ext[0].lower() in images:
        st.move(path + file, path + 'images/' + file)
    elif ext[0].lower() in docs:
        st.move(path + file, path + 'docs/' + file)
    elif ext[0].lower() in data:
        st.move(path + file, path + 'data/' + file)
    elif ext[0].lower() in code:
        st.move(path + file, path + 'code/' + file)
    else:
        st.move(path + file, path + 'misc/' + file)

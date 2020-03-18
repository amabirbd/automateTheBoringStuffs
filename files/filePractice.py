import shutil , os

from pathlib import Path

p = Path.home()

shutil.copy(p/'bacon.txt', p/'eggs/eggs2.txt')

shutil.move(p/'bacon.txt', p/'eggs/eggs2.txt')

# Permanently Deleting Files and Folders

# os.unlink(path) will delete the file at path.
# os.rmdir(path) will delete the folder at path. 
# shutil.rmtree(path) will remove the folder at path,
# and all files and folders it contains will also be deleted.

for filename in Path.home().glob('*.rxt'):
    os.unlink(filename)
    print(filename)

# Safe Deletes with the send2trash Module
import send2trash

send2trash.send2trash('bacon.txt')

# Walking a Directory Tree
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

# Compressing Files with the zipfile Module
import zipfile

exampleZip = zipfile.ZipFile(p/'example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
exampleZip.close()

# Extracting from ZIP Files
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall() #extracts file into the current directory
exampleZip.extract('spam.txt', 'anypath')
exampleZip.close()

# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


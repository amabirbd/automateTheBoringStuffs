import os
from pathlib import Path

hello = os.path.join('usr', 'bin', 'spam')
print(hello)

p = Path('spam', 'bacon', 'eggs')
print(p)
print(type(p))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\\user/hello', filename))

print(f'current working directory --> { Path.cwd() }')

os.chdir('C:\\Windows\\Temp\\')
print(f'after using chdir(change directory) --> { Path.cwd() }')

print(f'home directory -> {Path.home()}')

# relative path 
    # currnet directory -> .\
    # parent directory -> ..\


# absolute path
    # C:\
    # C:\Users

# Creating New Folders Using the os.makedirs() Function

#os.makedirs('C:\\delicious\\walnut\\waffles')
# to make a directory from a Path object

#Path(r'C:\Users\Al').mkdir()

print(Path.cwd().is_absolute())

# to get absolute path from relative path
print(Path('my/relative/path') )   #relative path
print(Path.cwd()/Path('my/relative/path')) #absolute path

print('os: ')
print(os.path.abspath('.'))

print(os.path.abspath('.\\Scripts'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))


p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
# p.parent, p.name, p.stem, p.suffix, p.drive

print('printing parents: ')
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])

# Directory and Base
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.sep))


# Finding File Sizes and Folder Contents
size = os.path.getsize('C:\\Windows\\System32\\calc.exe')
dirli = os.listdir('C:\\Windows\\System32')
#print(size)
#print(dirli)

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(f'total size {totalSize}')


# Modifying a List of Files Using Glob Patterns
p = Path('C:/Users/USER/Desktop')
p.glob('*')
#print(list(p.glob('*')))
print(list(p.glob('*.txt')))

list(p.glob('project?.docx')) # The glob expression 'project?.docx' will return 'project1.docx' or 'project5.docx', but it will not return 'project10.docx'
list(p.glob('*.?x?')) # The glob expression '*.?x?' will return files with any name and any three-character extension where the middle character is an 'x'.


# Checking Path Validity

# p.exists() returns True if the path exists or returns False if it doesn’t exist.

# p.is_file() returns True if the path exists and is a file, or returns False otherwise.

# p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.


# Reading files
p = Path('spam.txt')
p.write_text('Hello, world!')
print(p.read_text())

helloFile = open(Path.home()/ 'hello.txt') # create a file in your home directory
helloContent = helloFile.read()
print(helloContent)
# .readline() method


# Writing to Files

baconFile = open('bacon.txt', 'w')  # write mode
baconFile.write('Hello, world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')  # append mode
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()  # just read mode
baconFile.close()
print(content)


# Saving Variables with the shelve Module

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'simon']
shelfFile['cats'] = cats
shelfFile.close()

# Saving Variables with the pprint.pformat() Function

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
print(fileObj.write('cats = ' + pprint.pformat(cats) + '\n'))
fileObj.close()
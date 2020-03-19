# backup work in a zip file
import zipfile, os

def backupZip(folder):
    #backup the entire contents of "folder" into a Zip file
    folder = os.path.abspath(folder)

    # figure out which filename this code should use based on 
    # what files already exist.
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1
        # create the zip file
        print(f'Creating {zipFileName}...')
        backupZip = zipfile.ZipFile(zipFileName, 'w')

        print('done.')


    # create the zip file
    # walk the entire folder tree and compress the files in each folder

backupZip('C:\\delicious')
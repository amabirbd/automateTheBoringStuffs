# Renaming Files with American-Style Dates to European-Style Dates

import shutil, os, re

datePattern = re.compile(r"""
    ((0|1)? \d)-        # one or two digits for month
    ((0|1|2|3)?\d)-     # one or two digit for day
    ((19|20)\d\d)       # four digits for year
    (.*?)$              # all text after date
    """
    )

#loop over the files in the working directory
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)
    print(mo)
    print(f'amer - > {amerFileName}')
    # skip files without dates
    if mo == None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # rename the files
    print(f'Renaming"{amerFileName}" to "{euroFileName}"...')
    shutil.move(amerFileName, euroFileName)
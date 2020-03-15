import re

with open('data.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

    # 568-555-6051
    phoneRegex = re.compile(r'(\d\d\d)(-|\s)(\d\d\d)(-|\s)(\d\d\d\d)')

    mo = phoneRegex.findall(f_contents)
    print(mo[0])
    
    for i in mo[0]:
        print(i)
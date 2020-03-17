#password locker program

PASSWORD = {
            'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'
        }

import sys, pyperclip
if len(sys.argv) < 2:
    print(('Usage: py pw.py [account] - copy account password'))
    sys.exit()

account = sys.argv[1] 

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('there is no account name' + account)
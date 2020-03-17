# Want to know how to keep an idiot busy for hours?

import pyinputplus as pp

while True:
    response = pp.inputStr(prompt="Want to know how to keep an idiot busy for hours?")

    if response == 'no':
        print(f"Thank you. Have a nice day.")
        break
    elif response == 'yes':
        pass
    else:
        print(f'{response} is not a valid answer, type "yes" or "no" ')

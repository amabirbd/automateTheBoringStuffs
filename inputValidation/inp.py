import pyinputplus as pyip

resposne = pyip.inputNum()

# The min, max, greaterThan, and lessThan Keyword Arguments
response = pyip.inputNum('Enter num: ', min=4)
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('>', min=4, lessThan=6)

# The blank Keyword Argument
response = pyip.inputNum(blank=True)

# The limit, timeout, and default Keyword Arguments
response = pyip.inputNum(limit=2) # two attempts
response = pyip.inputNum(timeout=10) # will wait for 10 seconds for input 
response = pyip.inputNum(limit=2, default='N/A')

# The allowRegexes and blockRegexes Keyword Arguments
response = pyip.inputNum(allowRegexes=[r'(I|X|L|C|D|M)+', r'zero'])
response = pyip.inputNum(allowRegexes=[r'(i|x|l|c|d|m)+', r'zero'])
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])

# Passing a Custom Validation Function to inputCustom()
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
        if sum(numbersList) != 10:
            raise Exception('the digits must add up to 10 , not %s' %(sum(numbersList)))
        return int(numbers)

res = pyip.inputCustom(addsUpToTen)
print(res)

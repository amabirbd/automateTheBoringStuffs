import re

phoneNumRegex = re.compile(r'(\d\d\d)(\d\d\d\d\d\d\d\d)')

mo = phoneNumRegex.search('my num is 01837362265')

vendor, other = mo.groups()


print('phone num: ' + mo.group())
print(f'first three digits {vendor}')

#mumluiple groups with pipe
batRegex = re.compile(r'Bat(man|mobile|copter)')

mo1 = batRegex.search('Batmobile lost a wheel')

print(mo1.group(1))

#optional matching with ( ? )
batRegex1 = re.compile(r'Bat(wo)?man')
mo2 = batRegex1.search('The Adventures of Batman')
print(mo2.group())

# matching 0 or more with ( * )
batRegex2 = re.compile(r'Bat(wo)*man')
mo3 = batRegex2.search('The Adventures of Batwowowoman')
print(mo3.group())

# matching 1 or more with ( + )
batRegex3 = re.compile(r'Bat(wo)+man')
mo4 = batRegex2.search('The Adventures of Batwoman')
print(mo4.group())

# marching specific repetitions eith curly brackets
haRegex = re.compile(r'(Ha){3}') # {lowerBound : upperBound}
haRegex1 = re.compile(r'(Ha){2,5}')
mo6 = haRegex1.search('HaHa')
# if a search is unmatched it returns a Nonetype object
if mo6 is None:
    print("None")
else:
    print('not None')

#greedy and none greedy regex

# in the below example both the matches are valid 
# match and returns longest possible str
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo7 = greedyHaRegex.search('HaHaHaHaHa')
print(mo7.group())

# match shortest possible str
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo8 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo8.group())

# findall method will search all the matches and return them as a list obj

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\d\d\d\d')
mo9 = phoneNumRegex.findall('cell1: 018-37362265 , cell2: 018-03242424')
print(mo9)

# shorthand character classes

# \d -> any numeric digit from 0-9
# \D -> any character that is not a numeric digit from 0-9
# \w -> any letter, numeric digit or the underscore character
#       word character
# \W -> any character that is not a letter , numeric digit
#       or the underscore character
# \s -> any space , tab or newline character. (space )
# \S -> any character that is not a space , tab or newline.


# custom regex
# have to use square brackets

vowelRegex = re.compile(r'[aeiouAEIOU]')
v = vowelRegex.findall('RoboCop eats baby food. BABY FOOD')
print(v)

vowelRegex1 = re.compile(r'[a-zA-Z0-9]')
v2 = vowelRegex1.findall('RoboCop eats baby food. BABY FOOD')
print(v2)

# carret sign ( ^ ) -> string must start with the following text
# dollar sign ( $ ) -> string must end with the following text

beginsWithHello = re.compile(r'^Hello')
bw = beginsWithHello.search('Hello World')
print(bw)

# matches string starting with one or more word and then ending with one or more number

wholeStringIsNum = re.compile(r'^\w+\d+$')
w = wholeStringIsNum.search('wler12345')
print(w)

# wildcard character ( . ) 

atRegex = re.compile(r'.at')
a = atRegex.findall('The cat in the hat sat on the flat mat.')
print(a)

#matching everything with ( .* )

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.groups())
print(mo.group())
print(mo.group(1))

# (.*) method is greedy by nature , to use a non greedy version use (.*?)
nonGreedyRegex = re.compile(r'<.*?>')
ng = nonGreedyRegex.search('<To serve man > for dinner.>')
print(ng.group())

# Matching Newlines with the Dot Character
# The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character

NewlineRegex = re.compile('.*', re.DOTALL)
nl = NewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
print(nl)

#case insensitive matching
robocop = re.compile(r'robocop', re.I)
r = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(r)

# Substituting Strings with the sub() method 
namesRegex = re.compile(r'Agent \w+')
n = namesRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.')
print(n)

agentNameRegex = re.compile(r'Agent (\w)\w*')
ag = agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(ag)

# Instead of this 
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4} (\s*(ext|x|ext.)\s*\d{2,5})?)')

# Do this
phoneRegex = re.compile(r'''
(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?          # separator
    \d{3}               # first three digits
    (\s|-|\.)           # separator
    \d{4}               # last four digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    
)
''', re.VERBOSE)

# combining re.ignorecASe, re.dotAll, and re.VerBoSe

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)



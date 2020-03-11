s = "Hello world"

print(len(s))
print(str(reversed(s))) #creats an obj

print(s.upper())
print(s.lower())
print(s.capitalize())

print(f"There are {s.count('o')} 'o's in the string")

print(s[2:5])
print(s[::2])
print(s[::-1]) # reverse the string using list slicing

print(s.isalnum())  #islpha, isnum, isdecimal, istitle...


print(s.startswith('h'))
print(s.endswith('e'))

print(', '.join(['cats', 'rats', 'bats', s]))
print(s.split())
print(s.split('o')) #split where there's a 'o'
print("      striping 6 space on left 1 on right ".strip()) #there are also 'rstrip' and 'lstrip'

print("hello".rjust(10,'*')) #adds 10 space like padding
print("hello".ljust(10,'*'))
print("hello".center(35, '#')) 

def printPicnic(itemsDict, leftWtidth, RightWidth):
    print('PICNIC ITEMS'.center(leftWtidth + RightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWtidth, '.') + str(v).rjust(RightWidth))

picnicItems = {'sandwiches': 4, 'apples':12, 'cups':4, 'cookies':8000}
print(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


import re
import os

text_to_search = '''
Ha HaHa Ha

abcdefghijklmn

1234567890

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyems.com
800.499.6739
900-346-5234

123.499.6739
321-346-5234
123*-499*-6739

cat
mat
bat
pat

Mr. Li
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'abc')
pattern = re.compile(r'\bHa') # search for character with word boundary
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # Search for the phone number
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # Same function as last line

pattern = re.compile(r'\d\d\d[.]\d\d\d[.]\d\d\d\d')
pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
pattern = re.compile(r'[^0-5a-zA-z]') # ^ means not inside the square brackets
pattern = re.compile(r'[^b]at')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # Every person's name starting with 'Mr.' or 'Mr'
pattern = re.compile(r'M(r|rs|s)\.?\s[A-Z]\w*') # All person's name in the text

matches = pattern.finditer(text_to_search) # Comes with an extra function of group feature compared with fillall()
matches2 = pattern.findall(text_to_search) # Prints solely the 1st matched group of text or if grouped

# print(matches2)

for match in matches:
    print(match)

### Load a file of numbers and grab all the matched number.
# pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')
# dir_path = os.path.dirname(os.path.realpath(__file__))

# with open(os.path.join(dir_path, 'data.txt'), 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)



sentence = 'Start a sentence and then bring it to an end'
pattern2 = re.compile('^Start')
pattern2 = re.compile(r'end$')
matches2 = pattern2.finditer(sentence)

# for match in matches2:
#     print(match)

pattern = re.compile(r'Start')
pattern = re.compile(r'start', re.IGNORECASE) # Ignore the cases with an extra flag, re.I or re.IGNORECASE both work
matches = pattern.match(sentence)
pattern = re.compile(r'sentence')
matches = pattern.search(sentence)
print('Sentences: ', matches)



emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z]+@[a-zA-z]+\.com')
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-z.]+\.(com|edu)')
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-z.-]+\.(com|edu|net)')
matches = pattern.finditer(emails)

# for match in matches:
#     print(match)





urls = '''
https://www.google.com
https://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)
for match in matches:
    print(match.group(0)) # The entire group match
    # print(match.group(1)) # 1st group match

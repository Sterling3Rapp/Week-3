import re

s = "My phone number is (443)907-4060"

phoneNumberPattern = re.compile(r'''
(\(?\d(3)\)?(-| |\.)?)?
\d(3)-
\d(4)''',re.VERBOSE)
resultObject = phoneNumberPattern.search(s)
print(resultObject.group())


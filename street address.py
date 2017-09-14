import re

s = "1 Seahawk Dr 123 Main Street 20 Sycamore Ln "

address = re.compile(r'\d+ \w {2}')

result = address.findall(s)
print = result
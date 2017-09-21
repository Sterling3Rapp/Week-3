import requests
import bs4
import re

r = requests.get('http://classifieds.delawareonline.com/map.php?place=Garage+Sales&posit=Garage+Sales')
soup = bs4.BeautifulSoup(r.content,'html.parser')
s = str(soup)
street = "20 Sycamore Ln 123 Main St 5987 Carriage Ct"

address = re.compile(r'\d+\s\w+\s\w{2}')
result = address.findall(street)
yardsales = address.findall(s)

print(result)
print(yardsales)

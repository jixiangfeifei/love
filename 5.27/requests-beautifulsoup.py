
import requests

r = requests.get("http://www.python123.io./ws/demo.html")

demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")

print (soup.prettify())

print (soup.head)
print (soup.head.contents)

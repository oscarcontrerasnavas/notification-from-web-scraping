"""Small script to send me an email once it found the page was updated
"""

from requests import get
from filecmp import cmp

# Get the current state of the website
url = "http://portal.senasofiaplus.edu.co/index.php/cronograma"
new_page = get(url).text
file = open("new-page.txt", "w+")
file.write(new_page)
file.close()

# Compare with the old version
if not(cmp("old-page.txt", "new-page.txt")):
    pass
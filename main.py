"""Small script to send me an email once it found the page was updated
"""

from requests import get
from filecmp import cmp
import os
import smtplib

# Get the current state of the website
url = "http://portal.senasofiaplus.edu.co/index.php/cronograma"
new_page = get(url).text
file = open("new-page.txt", "w+")
file.write(new_page)
file.close()

# Compare with the old version
if not(cmp("old-page.txt", "new-page.txt")):

    # Connecting to the gmail server using a context manager
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo() # Start connection
        smtp.starttls() # Start encriptation
        smtp.ehlo() # Restart the connection to the server but encripted

        # Getting credentials from my environment variables
        EMAIL_ADDRESS = os.environ.get('EMAIL_USER') 
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "The SENA.EDU.CO calendar has changed."
        body = "This is an automatic email set up for you to get the last update."

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

else:
    os.remove("old-page.txt")
    os.rename("new-page.txt", "old-page.txt")
    print("The website has not been updated.")        
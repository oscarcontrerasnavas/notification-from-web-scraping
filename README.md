# Get an email notification when the website you targeted was updated

So, I google and write some code to send to myself an automatic email every time
a specific website is modified. The script is also attached to a batch file for
the windows console (CMD) and I have created a schedule for it so it runs
every day at noon and keeps me on track.

## main.py

The script make use of the following libraries:

* `requests` to get the page with the url address.
* `filecmp` to check if two files are equal bit by bit.
* `os` to delete and rename files and also to import some credentials from the environment variables.
* `smtplib` to set the gmail connection and send the mail.

```python
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
```

I still consider myself as a noob when it is related to coding but I feel the script is self-explanatory. However if you have some doubts, please don't hesitate to dm me.
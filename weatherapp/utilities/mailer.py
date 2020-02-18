import os
import smtplib
from email.message import EmailMessage

EMAIL_ID = os.environ.get('EMAIL_ID')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
msg = EmailMessage()
msg['Subject'] = 'Discount on us'
msg['From'] = EMAIL_ID
msg['To'] = 'vedantpuri@umass.edu'
msg.set_content('How about a discount on us')


# context manager snures connection is closed automatically
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as conn:
    conn.login(EMAIL_ID, EMAIL_PASS)
    conn.send_message(msg)

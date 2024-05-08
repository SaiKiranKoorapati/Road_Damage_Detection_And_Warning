import urllib.request
import time
import requests




url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=Crack detected Drive Safely  &language=english&route=p&numbers=8801915140"
headers = {
                'authorization': "doHXTuKtW2371lpp6MzeHXefoxdXIvSWKyzTmrPluqFWIJan3nKu0LtRFZCJ",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                }
response = requests.request("POST", url, data=payload, headers=headers)
print("SMS Sent successfully")

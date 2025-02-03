import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import pandas as pd
import datetime

URL = "https://www.amazon.in/Samsung-Inverter-Fully-Automatic-WA70BG4441YYTL-Technology/dp/B0B8NHX62W/ref=sr_1_3?crid=TWB1O87EYHD4&dib=eyJ2IjoiMSJ9.1XALfXgJxk24Mo-mL4AuxP4qvB6wbZ6OB4P6rluGv_7xYlcVJbLOOYMKDpncqEEP0N2NcXcdLZvNurzG7utRRJRy-qKPVtC8mi908AynUb1PUKMTg8xs15HlJNEqCJmalkq04k9D7LZbur-lKxaT8Wk4nAglvBI0_yfRFy6MY2b0hMbaPrZFvj59tLmIOAmUeOls7-zrmGRBBMKaGbVUyI91FmbmUWPrI8SWCpDvPd0.Wh2ENL7GSY7_PCERw52QsZt-sZJylwBHqUtXNM4BbQI&dib_tag=se&keywords=washing%2Bmachine%2Bsamsung&nsdOptOutParam=true&qid=1738244962&sprefix=washing%2Bmachine%2Bsam%2Caps%2C222&sr=8-3&th=1"
TWILIO_SID = "unique Twilio account SID"
TWILIO_AUTH = "Unique twilio account authentication id"
TWILIO_PHONE = "phone number given by twillio"
USER_PHONE = "registered phone number on twilio"
PRICE_MAX = 18000                                                             #maximum price of product according to budget
FILE_PATH_CSV = r"D:\Documents\price_record.csv"                              #filepath where the document must be saved

#Getting the contents of the web page using requests module
response = requests.get(url=URL)
data = response.text

#Scraping the website
soup = BeautifulSoup(data, "html.parser")
price_whole = soup.find("span", class_="a-price-whole").getText()
product_name = soup.find("span", id="productTitle").getText()

#Conversion into float number

price_lst = price_whole.split(".")
price_lst_fin = price_lst[0].split(",")
price = int("".join(price_lst_fin))
print(price)

#Setting up twilio and sendiing message using twilio
client = Client(TWILIO_SID, TWILIO_AUTH)

# #Drafting a message
if(price <= PRICE_MAX):
    message = client.messages.create(
        body=f"The price of the {product_name} is now {price}. Buy now!",
        from_=TWILIO_PHONE,
        to=USER_PHONE
    )

#Appending the data into CSV
date = [str(datetime.date.today())]
price_lst = [price]
new_entry = pd.DataFrame({"date" : date, "price":price_lst})
new_entry.to_csv(FILE_PATH_CSV, index=False, header=False, mode="a")


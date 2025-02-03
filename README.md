# Amazon_price_tracker
This project uses python web scraping and alerts the user about the price drop of a specific product through SMS

The user can specify the product to be brought from amazon using an url to the product web page.
The python 'requests' module is used to get hold of the data on that page.
This project uses 'BeautifulSoup' to scrape the amazon website and obtain product name and its price.
The price is then compared with the maximum price the user is willing to pay for the given product. 
If this price is less than the maximum price, the program sends notification to the user alerting him to buy the product using the 'twilio' API.
The program also gets the price of the product at different dates when program is run and stores them in CSV format which can later be used to analyze the trends of rise ad fall of product price.
